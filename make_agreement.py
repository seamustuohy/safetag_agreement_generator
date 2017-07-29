from os import path
from jinja2 import Template, Environment, FileSystemLoader
import subprocess

def render(tpl_path, context):
    fpath, filename = path.split(tpl_path)
    env = Environment(loader=FileSystemLoader(fpath or './'))
    tmp = env.get_template(filename)
    return tmp.render(context)

def main():
    from variables.plain_fill_in import objects as fill_in_vars
    from variables.plain_example import objects as example_vars

    # Create fill in template
    res = render("templates/plain.j2", fill_in_vars)
    md_path = "outputs/plain_fill_in.md"
    compose_agreement(md_path, res)
    pdf_path = "outputs/plain_fill_in.pdf"
    pandoc_command = ["pandoc", "-f", "markdown_github", "-t", "latex", "-o", pdf_path, md_path]
    subprocess.check_call(pandoc_command)

    # Create example
    res = render("templates/plain.j2", example_vars)
    md_path = "outputs/plain_example.md"
    compose_agreement(md_path, res)
    pdf_path = "outputs/plain_example.pdf"
    pandoc_command = ["pandoc", "-f", "markdown_github", "-t", "latex", "-o", pdf_path, md_path]
    subprocess.check_call(pandoc_command)

def compose_agreement(output_path, render):
    with open(output_path, 'w+') as write_file:
        write_file.write(render)

if __name__ == '__main__':
    main()
