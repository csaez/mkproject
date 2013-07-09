from string import Template
import os
import sys


def _mkfile(project_name, src_file, dst_file):
    with open(src_file) as f:
        contents = f.read()
    contents = Template(contents).substitute(name=project_name)
    with open(dst_file, "w") as f:
        f.write(contents)


def _mkdir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def main():
    project_dir = sys.argv[1]
    project_name = os.path.basename(project_dir)

    # create dir
    _mkdir(project_dir)
    _mkdir(os.path.join(project_dir, project_name))
    _mkdir(os.path.join(project_dir, project_name, "tests"))
    _mkdir(os.path.join(project_dir, "bin"))
    _mkdir(os.path.join(project_dir, "docs"))

    # files
    templates = os.path.join(os.path.dirname(__file__), "templates")
    _mkfile(project_name,
            os.path.join(templates, "setup.py"),
            os.path.join(project_dir, "setup.py"))
    _mkfile(project_name,
            os.path.join(templates, "CHANGES.txt"),
            os.path.join(project_dir, "CHANGES.txt"))
    _mkfile(project_name,
            os.path.join(templates, "LICENSE.txt"),
            os.path.join(project_dir, "LICENSE.txt"))
    _mkfile(project_name,
            os.path.join(templates, "MANIFEST.in"),
            os.path.join(project_dir, "MANIFEST.in"))
    _mkfile(project_name,
            os.path.join(templates, "README.md"),
            os.path.join(project_dir, "README.md"))
    _mkfile(project_name,
            os.path.join(templates, "name_test.py"),
            os.path.join(project_dir, project_name, "tests", project_name + "_test.py"))
    _mkfile(project_name,
            os.path.join(templates, "__init__.py"),
            os.path.join(project_dir, project_name, "tests", "__init__.py"))
    _mkfile(project_name,
            os.path.join(templates, "__init__.py"),
            os.path.join(project_dir, project_name, "__init__.py"))

__all__ = [main]
