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


import re
import json
import datapackage

# =============================================================
# DEPRECATED and INCOMPLETE Text Based User Interface Code
# =============================================================
# Included in repository to save the safetag agreement data file
# parsing code that was created to support it. Some functionality
# has not been included in the current GUI. This code can help in
# providing that functionality in the future.
# .............................................................

# Set decision object globally
Decision = namedtuple("Decision", ["question",
                                   "help",
                                   "sets",
                                   "depends",
                                   "answers",
                                   "from_package"])



class tcol:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def load_decisions(input_path):
    with open(input_path, "r") as fp:
        decisions = json.load(fp)
    return decisions

def get_answer(question):
    print(tcol.OKBLUE + tcol.BOLD + question.get("question", "QUESTION NOT DEFINED") + tcol.ENDC)
    response = None
    help_text = question.get("help", None)
    if help_text is not None:
        print(tcol.OKGREEN + "\"{0}\"".format(help_text) + tcol.ENDC)
    if question.get("take_input", True) is not False:
        answers = question.get("answers", {})
        lower_answers = [k.lower() for k in answers.keys()]
        if answers == {}:
            response = input("Enter your answer here: ")
        else:
            by_num = {}
            print("Please choose from the following")
            i = 1
            for k, v in answers.items():
                print("({0}) {1}".format(i, k))
                by_num[i] = k
                i += 1
            while response is None:
                choice = input("Enter your answer here: ")
                if answers.get(choice, None) is not None:
                    response = answers.get(choice)
                elif choice.lower() in lower_answers:
                    for i in answers.keys():
                        if i.lower() == choice.lower():
                            response = answers.get(i)
                else:
                    try:
                        int_ans = int(choice)
                        response_item = by_num.get(int_ans, None)
                        if response_item is None:
                            raise ValueError("Invalid Number")
                        response = answers.get(response_item)
                    except ValueError:
                        print(tcol.WARNING + "Sorry, that was an invalid choice" + tcol.ENDC)
    elif question.get("from_package", None) is not None:
        return evaluate_from_package(question, get_datapackage_path())
    return response


def get_datapackage_path():
    """TODO Eventually this should parse from an env or config file"""
    return 'variables/datapackage.json'


def evaluate_from_package(package_data, datapackage_path):
    package_name = package_data.get('name', None)
    pkg = datapackage.Package(datapackage_path)
    resource = pkg.get_resource(package_name)
    data = resource.table.read(keyed=True)
    # Check for conditional data
    # Conditions use an AND operation when provided multiple
    conditions = package_data.get("conditions", None)
    if conditions is None:
        return data
    else:
        requested = []
        for resource_table in data:
            found_false = False
            for k, v in conditions.items():
                if resource_table.get(k) != v:
                    found_false = True
            if found_false is True:
                requested.append(resource_table)
        return requested

def test_get_answer():
    print("Basic yes/no")
    question = {"question": "What guidelines do you have for gathering, storing, and destroying confidential information and test data?",
                "help": "I am help text that exists",
                "sets": "test_question_item",
                "answers": {"Yes": True, "No": False}}
    response = get_answer(question)
    print("\nYou choice answer: {0}".format(response))
    # No input
    print("\nNo Input Required")
    question['take_input'] = False
    response = get_answer(question)
    print("\nYou choice answer: {0}".format(response))
    # No answers provided
    print("\nChoose your own long form answer")
    question['take_input'] = True
    question['answers'] = {}
    response = get_answer(question)
    print("\nYou choice answer: {0}".format(response))


def get_decisions(path):
    with open(path) as decision_io:
        decisions = json.load(decision_io)
    return decisions



def set_decision(decision, response=None):
    if decision.sets == "":
        raise ValueError("A decision needs to set something")
    # From Package
    if decision.from_package != {}:
        _parsed_fp = evaluate_from_package(decision.from_package,
                                           get_datapackage_path())
        return {decision.sets, _parsed_fp}
    else:
        return {decision.sets, response}

def parse_decision(raw_decision):
    decision = Decision(
        question=raw_decision.get("question", ""),
        answers=raw_decision.get("answers", {}),
        sets=raw_decision.get("sets", ""),
        depends=raw_decision.get("depends", {}),
        help=raw_decision.get("help", ""),
        from_package=raw_decision.get("from_package", {}))
    return decision


def test_evaluate_from_package():
    eval_string = {
        "name": "data_handling",
        "conditions": {
            "reponsible_parties":"service_provider",
            "security_focus": "devices"}}
    pkg_pth = 'variables/datapackage.json'
    req = evaluate_from_package(eval_string, pkg_pth)
    print(req)


def test_decisions(path):
    raw = get_decisions(path)
    # print([(i, len(v)) for i,v in raw.items()])
    for section, questions in raw.items():
        print(tcol.HEADER + re.sub("_", " ", section) + tcol.ENDC)
        for question in questions:
            get_answer(question)
