#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    # indent to keep dnsfile open
    #loop across lines of file
    for svr in dnsfile:
        svr = svr.rstrip('\n') # remove new line char if exists
                               # would exist on all but last line

        # if the string svr ends with 'org'
        if svr.endswith('org'):
            with open("org_domain.txt", "a") as srvfile:
                    srvfile.write(svr + "\n")
        # ELSE IF the string svr ends with 'com'
        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:
                srvfile.write(svr + "\n")


