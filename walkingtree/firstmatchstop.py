#!/usr/bin/env python3

## scripto to search and stop onm first match

import os

## define a fuction that stops the searching on first match

def find(name, path):
    for root, dirs, files in os.walk(path):
        if name in files:
            return os.path.join(root, name)

lookfor = input("what am i looking for?  ")
lookwhere = input("what is the path in which I should search? ")

print(find(lookfor, lookwhere))


