#!/usr/bin/env python

import os


HEADER="""# TIL

> Today I Learned


A collection of software engineering tips that I learn every day.

---

### Categories

"""



def main():
    content = ""
    content += HEADER

    for root, dirs, files in os.walk("asd"):
        print(root)




if __name__ == "__main__":
    main()
