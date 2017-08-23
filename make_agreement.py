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

from os import path
from jinja2 import Template, Environment, FileSystemLoader, StrictUndefined
import subprocess
import json

def main():
    create_plain()
    create_explicit()

def render(tpl_path, context):
    fpath, filename = path.split(tpl_path)
    env = Environment(loader=FileSystemLoader(fpath or './'), undefined=StrictUndefined)
    tmp = env.get_template(filename)
    return tmp.render(context)

def create_plain():
    from variables.plain_example import objects as example_vars

    # Create example
    res = render("templates/plain.j2", example_vars)
    md_path = "outputs/plain_example.md"
    compose_agreement(md_path, res)
    pdf_path = "outputs/plain_example.pdf"
    pandoc_command = ["pandoc", "-V", "geometry:margin=1in", "-f", "markdown_github", "-t", "latex", "-o", pdf_path, md_path]
    subprocess.check_call(pandoc_command)

def create_explicit():
    from variables.explicit_example import objects as example_vars

    # Create example
    res = render("templates/explicit.j2", example_vars)
    md_path = "outputs/explicit_example.md"
    compose_agreement(md_path, res)
    pdf_path = "outputs/explicit_example.pdf"
    pandoc_command = ["pandoc", "-V", "geometry:margin=1in", "-f", "markdown_github", "-t", "latex", "-o", pdf_path, md_path]
    subprocess.check_call(pandoc_command)

def load_decisions(input_path):
    with open(input_path, "r") as fp:
        decisions = json.load(fp)
    return decisions

def create_graph(decisions):
    raise NotImplementedError("")

def compose_agreement(output_path, render):
    with open(output_path, 'w+') as write_file:
        write_file.write(render)

if __name__ == '__main__':
    main()
