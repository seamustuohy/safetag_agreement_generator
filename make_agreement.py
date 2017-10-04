#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# This file is part of safetag agreement generator, a assessment agreement generator.
# Copyright © 2017 seamus tuohy, <code@seamustuohy.com>
#
# This program is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by the Free
# Software Foundation, either version 3 of the License, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the included LICENSE file for details.
import logging
from os import path
from jinja2 import Template, Environment, FileSystemLoader, StrictUndefined
import subprocess
import json
from collections import namedtuple
from typing import Dict, NamedTuple
import datapackage
from datetime import datetime
import copy
import argparse
import re
import tkinter as tk
from tkinter import font


import pygraphviz as pgv
import networkx as nx

# =======================
# Graph Viz
# =======================

def create_graph(decision_path):
    G = nx.DiGraph()
    G.graph['label'] = 'SAFETAG Agreement Decision Path'
    with open(decision_path) as decision_io:
        decisions = json.load(decision_io)
    edges = []
    root_node_name = "safetag_agreement"
    G.add_node(root_node_name)
    nodes_subgraphs = {"sections": []}
    for section, questions in decisions.items():
        depends_level = {}
        depends_tree = {}
        node = G.add_node(section)
        # add section to eventual section subgraph
        nodes_subgraphs['sections'].append(section)
        node = G.node[section]
        node['label'] = section
        node["shape"]="box"
        node["style"]="filled"
        node["fillcolor"]="white"
        edges.append((root_node_name, section, ""))
        for question in questions:
            question_sets = question['sets']
            G.add_node(question_sets)
            node = G.node[question_sets]
            node['label'] = question.get('question')
            node["shape"]="box"
            node["style"]="filled"
            node["fillcolor"]="white"
            node['tooltip'] = question.get('help', '')
            # Check dependencies
            dependencies = question.get('depends', {})
            if dependencies != {}:
                for depends_on, depends_value in dependencies.items():
                    if depends_on != "type":
                        edges.append((depends_on,
                                      question_sets,
                                      depends_value))
                        depends_level.setdefault(question_sets, 0)
                        depends_level[question_sets] += 1
                        depends_tree.setdefault(question_sets, [])
                        depends_tree[question_sets].append(depends_on)
            else:
                edges.append((section, question_sets, ""))
                # Add node to section subgraph
                nodes_subgraphs.setdefault(section, []).append(question_sets)
        dep_subgraphs = {}
        for quest_name, quest_deps in depends_tree.items():
            current_dep_num = 0
            for dep in quest_deps:
                current_dep_num += depends_level.get(quest_name, 0)
            dep_subgraphs.setdefault("{0}_{1}".format(section, current_dep_num),
                                     []).append(quest_name)

    for edge in edges:
        G.add_edge(edge[0],
                   edge[1],
                   label=edge[2])
    A = nx.nx_agraph.to_agraph(G)
    # Make sections top level item
    A.add_subgraph(nodes_subgraphs.get("sections"), rank=0)
    # Toss sections for same ranking
    toss_sections = nodes_subgraphs.pop("sections")
    for i,subgraph_items in nodes_subgraphs.items():
        A.add_subgraph(subgraph_items, rank='same')
    A.draw('outputs/decision_tree.svg', prog='dot', args="-Grankdir=LR")


# =======================
# Template Creation Code
# =======================


def render(tpl_path, context):
    fpath, filename = path.split(tpl_path)
    env = Environment(loader=FileSystemLoader(fpath or './'),
                      undefined=StrictUndefined)
    tmp = env.get_template(filename)
    return tmp.render(context)


def compose_agreement(output_path, render):
    with open(output_path, 'w+') as write_file:
        write_file.write(render)


def evaluate_depends(depends, state):
    depends = copy.deepcopy(depends)
    if len(depends) == 1:
        key, val = depends.popitem()
        cur_state = state.get(key, None)
        if cur_state is None:
            return None
        if cur_state == val:
            return True
    # If no type given then type == "and"
    elif depends.get("type", None) is None:
        for key, val in depends.items():
            cur_state = state.get(key, None)
            if cur_state is None:
                return None
            elif cur_state != val:
                return False
        return True
    elif depends.get("type", None) is not None:
        cond = depends.pop("type")
        conditions = set()
        for key, val in depends.items():
            # Check for question not asked yet
            cur_state = state.get(key, None)
            if cur_state is None:
                return None
            conditions.add(state.get(key, "") == val)
        if (cond == 'and') and conditions == set([True]):
            return True
        if (cond == 'or') and True in conditions:
            return True
    return False


def create_custom(base_fp, agreement_type="both"):
    # Set "both" agreement type
    if agreement_type == "both":
        agreement_type = ["plain", "explicit"]
    else:
        agreement_type = [agreement_type]
    # TODO: Add a plain/explicit question to the front of GUI and to this...
    # ... this will choose the questions to ask and format to print
    base_data = json.load(base_fp)
    # TODO: The code exists to parse the correct datapackage data from the decisions list
    #       But, the current Jinja templates just take directly from the datapackage
    #       Eventually we want to just use the decisions template.
    # Append Datapackages to base_data
    try:
        pkg = datapackage.Package(get_datapackage_path())
        for name in pkg.resource_names:
            log.debug("loading datapackage {0}".format(name))
            resource = pkg.get_resource(name)
            base_data[name] = resource.table.read(keyed=True)
    except datapackage.exceptions.CastError as _e:
        log.debug("Error while attempting to read datapackage resource")
        log.error(_e.errors)
        raise _e
    if "plain" in agreement_type:
        # Create plain
        res = render("templates/plain.j2", base_data)
        md_path = "outputs/plain_custom.md"
        compose_agreement(md_path, res)
        pdf_path = "outputs/plain_custom.pdf"
        pandoc_command = ["pandoc", "-V", "geometry:margin=1in",
                          "-f", "markdown_github", "-t",
                          "latex", "-o", pdf_path, md_path]
        subprocess.check_call(pandoc_command)
    if "explicit" in agreement_type:
        # Create Explicit
        res = render("templates/explicit.j2", base_data)
        md_path = "outputs/explicit_custom.md"
        compose_agreement(md_path, res)
        pdf_path = "outputs/explicit_custom.pdf"
        pandoc_command = ["pandoc", "-V", "geometry:margin=1in",
                          "-f", "markdown_github", "-t",
                          "latex", "-o", pdf_path, md_path]
        subprocess.check_call(pandoc_command)
    print("DONE")


def get_datapackage_path():
    """TODO Eventually this should parse from an env or config file"""
    return 'variables/datapackage.json'

# ====================================
# GUI for Safetag Agreement Generation
# ====================================


class Application(tk.Frame):
    default_theme = {
        "background": '#FFFFFF',
        "foreground": "#000000",
        "title_color": '#FFFFFF',
        "title_accent": '#2196F3',
        "font_size": 12,
        "font_family": "Robot"}

    def __init__(self, decision_path, master, theme=None, log=None):
        super().__init__(master)
        if log is None:
            def _logger(x):
                pass
            _log = namedtuple("log", ["debug", 'error', 'warn', 'info'])
            self.log = _log(_logger, _logger, _logger, _logger)
        else:
            self.log = log
        self.window = master
        # Get decision data
        with open(decision_path) as decision_io:
            self.decisions_to_make = json.load(decision_io)
        # Set theme
        if theme:
            self.theme = theme
        self.screen_width = int(master.winfo_screenwidth())
        self.screen_height = int(master.winfo_screenheight())
        master.minsize(height=self.screen_height, width=self.screen_width)
        master.maxsize(height=self.screen_height, width=self.screen_width)
        self.grid(sticky="nsew")
        self.set_theme()
        # ---  Outer Frame  ---
        #  _____________________
        # |                     |
        # |     Title           |
        # |---------------------|
        # |                     |
        # |    Inner Frame      |
        # |                     |
        # |---------------------|
        # |     Next Button     |
        # |_____________________|
        # Add Title to outer frame
        self.title = tk.Label(self,
                         background=self.theme["accent"],
                         foreground=self.theme["title_color"],
                         font=self.title_font,
                         wraplength=int((self.screen_width/3)*2))
        self.title.grid(column=0,
                        row=0,
                        sticky='new')
        # Add inner Frame within outer frame
        self.frame = tk.Frame(self,
                              bg=self.theme['background'],
                              height=self.screen_height/3,
                              width=self.screen_width)
        self.frame.grid(row=1,
                        pady=10,
                        sticky="ns")
        # Add Next button to outer frame
        submit_button = tk.Button(self,
                                  text="NEXT",
                                  background=self.theme["accent"],
                                  foreground=self.theme["title_color"],
                                  font=self.title_font,
                                  command=self.get_answer,
                                  relief="flat")
        submit_button.grid(column=0,
                           row=2,
                           sticky=tk.S)
        self.widgets = []
        self.answer_widgets = []
        self.decisions_made = {}
        self.current_set = []
        self.action_item = None
        self.next_decision()

    def set_theme(self):
        """ Resets the theme based on the self.theme object."""
        self.background = self.theme['main_background']
        self.foreground = self.theme['foreground']
        self.font = font.Font(family=self.theme['font_family'],
                              size=self.theme['font_size'],
                              weight="bold")
        self.title_font = font.Font(family=self.theme['font_family'],
                                    size=self.theme['font_size']+10,
                                    weight="bold")
        self.help_font = font.Font(family=self.theme['font_family'],
                                   size=self.theme['font_size'],
                                   slant="italic")
        self.configure(background=self.background)

    def destroy_widgets(self):
        """ Destroy all the question widgets to prepare for next question."""
        for widget in self.widgets:
            widget.destroy()
        for widget in self.answer_widgets:
            widget.destroy()
        self.widgets = []
        self.answer_widgets = []

    def write_answers(self):
        """Write the users answers into a custom agreement file."""
        present_time = datetime.now().strftime("%Y_%b_%d_%H_%M")
        with open("variables/custom_{0}.json".format(present_time), "w+") as custom_io:
            json.dump(self.decisions_made, custom_io)

    def action_select(self, var):
        """Sets the selected radio value as the answer for this question."""
        selection = "You selected the option " + str(var)
        self.log.debug(selection)
        self.action_item = var

    def get_answer(self):
        """Find the answer to the last question and store it """
        if len(self.answer_widgets) == 1:
            self.decisions_made[self.current_section][self.current_question] = self.answer_widgets[0].get("1.0",'end-1c')
        else:
            if self.action_item is None:
                self.action_item = False
            self.decisions_made[self.current_section][self.current_question] = self.action_item
        self.log.debug("ANSWER: {0}".format(self.decisions_made[self.current_section][self.current_question]))
        self.next_decision()


    def next_decision(self):
        """Iterates through all sections and questions to display questions.

           Main Question Runner.
        """
        if len(self.current_set) == 0:
            try:
                self.current_section, self.current_set = self.decisions_to_make.popitem()
                self.decisions_made.setdefault(self.current_section, {})
            except KeyError:
                # If we run out of sections than we are done
                self.write_answers()
                self.master.quit()
        # Check if a question has dependencies
        question_data = self.current_set.pop(0)
        self.log.debug("Current Question Data:\n{0}".format(question_data))
        self.current_question = question_data.get("sets")
        depends = question_data.get("depends", {})
        self.log.debug("QUESTION DEPENDS ON: {0}".format(depends))
        question_text = question_data.get("question", "")
        found = True
        if depends != {}: # Dependency exists!
            # Check for dependency found earlier in this section
            # Todo, allow dependencies to be found across sections
            self.log.debug(self.decisions_made[self.current_section])
            found = evaluate_depends(depends,
                                     self.decisions_made[self.current_section])
        if found is None:
            # Dependency has not been asked yet
            # We will push this question until later
            self.log.debug("Missing a question. Question {0} skipped".format(question_text))
            self.current_set.append(question_data)
            self.next_decision()
        elif found is False:
            # Dependency was asked and answer does not match
            # We don't need to ask this question
            self.log.debug("Dependency for {0} not met".format(question_text))
            self.decisions_made[self.current_section][self.current_question] = ""
            self.next_decision()
        else:
            # We can show this question!
            self.show_question(question_data)

    def show_question(self, question_data):
        """Cleans and Creates a question dialogue."""
        # Destroy any existing text widgets
        self.destroy_widgets()
        # Clean out old action items
        self.action_item = None
        # Set Title in outer frame
        self.title['text'] = self.current_section
        question_text = question_data.get("question", "")
        # ---  Inner Frame  ---
        #  _____________________
        # |                     |
        # |     question        |
        # |---------------------|
        # |     help text       |
        # |---------------------|
        # |     Answers         |
        # |_____________________|
        # Question
        question = tk.Label(self.frame,
                             background=self.theme['accent'],
                             foreground=self.theme['background'],
                             font=self.font,
                             wraplength=int((self.screen_width/3)*2))
        question['text'] = question_text
        question.grid(column=0,
                   row=1,
                   sticky='ew')
        self.widgets.append(question)
        # Help Text
        help_label = tk.Label(self.frame,
                             background=self.theme['background'],
                             foreground=self.foreground,
                             font=self.help_font,
                             wraplength=int((self.screen_width/3)*2))
        help_text = question_data.get("help", "")
        help_label['text'] = help_text
        help_label.grid(column=0,
                   row=2,
                   padx=10,
                   pady=10,
                   sticky=tk.N)
        self.widgets.append(help_label)
        # Answers (Default)
        # If multiple choice we provide radio choices
        default_answers = question_data.get("answers", {})
        if default_answers != {}:
            check_frame = tk.Frame(self.frame,
                                   bg=self.theme['background'],
                                   width=self.screen_width/2)
            check_frame.grid(column=0,
                             row=3,
                             padx=10,
                             pady=10,
                             sticky=tk.N)
            i = 0

            boolLabel = tk.BooleanVar()
            strLabel = tk.StringVar()
            for key, val in default_answers.items():
                if type(val) is bool:
                    radioVar = boolLabel
                else:
                    radioVar = strLabel
                _radio = tk.Radiobutton(check_frame,
                                        text=key,
                                        variable=radioVar,
                                        value=val,
                                        command=lambda : self.action_select(
                                            radioVar.get()))
                _radio.grid(column=0,
                            row=i,
                            padx=2,
                            pady=2)
                _radio.deselect()
                self.answer_widgets.append(_radio)
                i += 1
            self.widgets.append(check_frame)
        # Answers "free text"
        # If free text answer we provide a generic text input
        elif question_data.get("take_input", True) is True:
            text = tk.Text(self.frame)
            text.grid(column=0,
                      row=3,
                      padx=10,
                      pady=10,
                      sticky=tk.N)
            self.answer_widgets.append(text)
        # Answers: Data Package
        # If it's a datapackage we tell the user.
        # If they fill it out before finishing they will be included in the
        # auto-generated custom agreement.
        #
        # If not, they can just run this with the -p option to re-parse their
        # custom file
        else:
            package = question_data.get("from_package", {"name":"unknown"})
            package_name = package.get("name")
            datapackage_name = tk.Label(self.frame,
                                        background=self.theme["accent"],
                                        foreground=self.theme["background"],
                                        font=self.help_font,
                                        wraplength=int((self.screen_width/3)*2))
            datapackage_name['text'] = "This value is set in the {0} datapackage. You can update them and then complete this helper once you are done.".format(package_name)
            datapackage_name.grid(column=0,
                         row=3,
                         padx=10,
                         pady=10,
                         sticky=tk.N)
            self.widgets.append(datapackage_name)

        # Reconfigure frame size to fit with newly added objects
        self.grid_rowconfigure(0, weight=1, minsize=50)
        self.grid_rowconfigure(1, weight=0, minsize=self.screen_height/4*3)
        self.grid_rowconfigure(2, weight=1, minsize=50)
        self.grid_columnconfigure(0, weight=1, minsize=self.screen_width)

def set_logging(verbose=False, debug=False):
    if debug == True:
        log.setLevel("DEBUG")
    elif verbose == True:
        log.setLevel("INFO")

def parse_arguments():
    parser = argparse.ArgumentParser("Get a summary of some text")
    parser.add_argument("--verbose", "-v",
                        help="Turn verbosity on",
                        action='store_true')
    parser.add_argument("--debug", "-d",
                        help="Turn debugging on",
                        action='store_true')
    parser.add_argument("--parse", "-p",
                        help="Path to an existing custom agreement document to parse into an agreement. This will re-read the custom agreement values from this file as well as from the entity files. As such, this will execute the template without the decision tree questions. This enables you to tweak your agreement json file and/or your entity csv files to re-generate your agreements quickly.",
                        type=argparse.FileType('r'),
                        default=None)
    parser.add_argument("--agreement_type", "-a",
                        help="The type of agreement template to use. (plain, explicit, or both)",
                        default="both")
    parser.add_argument("--graph", "-g",
                        help="Create a decision tree graph",
                        action='store_true')
    args = parser.parse_args()
    return args

def main():
    # Collect Arguments
    args = parse_arguments()
    set_logging(args.verbose, args.debug)

    # If only parsing don't run GUI
    if args.parse is not None:
        create_custom(args.parse, args.agreement_type)
    # If making graph don't run GUI
    elif args.graph is True:
        create_graph(decision_path="variables/decisions.json")
    else:
        root = tk.Tk(className="Safetag")
        default_theme = {
            "main_background": root['bg'],
            "background": '#FFFFFF',
            "foreground": "#000000",
            "title_color": '#FFFFFF',
            "accent": '#2196F3',
            "font_size": 12,
            "font_family": "Robot"}
        app = Application(decision_path="variables/decisions.json",
                          master=root,
                          log=log,
                          theme=default_theme)
        app.mainloop()
        present_time = datetime.now().strftime("%Y_%b_%d_%H_%M")
        latest_custom = "variables/custom_{0}.json".format(present_time)
        with open(latest_custom) as fp:
            create_custom(fp, args.agreement_type)

if __name__ == '__main__':
    # Adding generic logging
    logging.basicConfig(level=logging.ERROR)
    log = logging.getLogger(__name__)
    main()
