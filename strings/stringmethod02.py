#!/usr/bin/env python3
"""Alta3 Research || Author: RZFreeser@alta3.com"""

def main():
    """ Run-time code"""
    # creat small string
    lilstring= "Alta3 Research offers classes on Python coding"
    newlist= lilstring.split(" ") #this returns the list
    print(newlist)

    # creat a list of strings
    myiplist= ["192", "168", "0", "12"]

    #set single IP as results of joining.....
    singleip= ".".join(myiplist)
    # display single IP
    print(singleip)


main()    
