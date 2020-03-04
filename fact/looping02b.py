#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep the dnsfile object open
    # create a list of lines
    dnslist = dnsfile.readlines()
    # loop over lines
    for svr in dnslist:
        # print and end without new line
        print(svr, end="")
# no need to clsoe file, closed auto
