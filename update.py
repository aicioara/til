#!/usr/bin/env python

import os


HEADER="""# TIL

> Today I Learned


A collection of software engineering tips that I learn every day.

---

"""


def main():
    content = ""
    content += HEADER

    for root, dirs, files in os.walk("."):
        if root == '.':
            try:
                dirs.remove('.git')
            except ValueError:
                pass
            continue

        category = os.path.basename(root)

        content += "### {}\n\n".format(category)

        for file in files:
            name = os.path.basename(file)
            name = " ".join(word.capitalize() for word in name.split('-'))
            content += "- [{}]({})\n".format(name, os.path.join(category, file))

    with open("README.md", "w") as fd:
        fd.write(content)


if __name__ == "__main__":
    main()
