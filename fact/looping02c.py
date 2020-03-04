#!/usr/bin/env python3
# opemd file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    for svr in dnsfile:
        print(svr, end="")

