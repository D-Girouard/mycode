#!/usr/bin/env python3

import os

import fnmatch

EXCLUDE = ["/usr", "/home", "/var"]

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE:
            dirs[:] = []
            files[:] = []
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

def main():
    lookfor = input("what pattern am i looking for (example: *.txt) ")
    lookwhere = input("where am i looking? ")
    print("results: ", find(lookfor, lookwhere))

main()


