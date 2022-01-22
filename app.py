import os
import os.path
from os import path
import re


def main():
    
    with open("a.txt") as file:
        files = file.readlines()
        l = os.path.join(os.getcwd(), "examples")
        print(l)
        for f in files:
            f = f.split("\n")[0]
            print(f)
            p = os.path.join(l, f)
            os.mkdir(p)
            p = os.path.join(p, "README.md")
            with open(p, 'w') as fp:
                pass
        if path.isfile(p):
            print("README.md created at " + p + " location")
        else:
            print("README.md creation FAILED at " + p + " location")


main()