#!/usr/bin/env python3
import os
def find_all(name, path):
    result = []
    for root, dirs, files in os.walk(path):
        if name in files:
            result.append(os.path.join(root, name))

    return result

lookfor = input("what am i looking for? ")
lookwhere = input("where am i looking? ")

print(find_all(lookfor, lookwhere))

