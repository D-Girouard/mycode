#!/usr/bin/env python3
# create a list of strings
vendors = ["cisco", "Juniper", "big_ip", "f5", "arista", "alta3", "zach", "stuart"]
# create a second list of strings
approved_vendors = ["cisco", "juniper", "big_ip"]
# loop across the list called vendors
for x in vendors:
    print("\nThe vendor is " + x, end="") # newline, print current vendor, and end without newline
    if x not in approved_vendors: # if x does no appear within the list 
        print(" - NOT AND APPROVED VENDOR!", end="")
print("\nOur loop has ended.") # print when loop has finished

