#!/usr/bin/env python3

# creating a small string
lilstring = "Alta3 Research offers classes on Python coding"
newlist = lilstring.split(" ") # this returns the list
print(newlist)

# creat list of strings
myiplist = ["192", "168", "0", "12"]

# set singleip as the resut of joining the list myiplist around the "."
singleip = ".".join(myiplist)

# display sinpleip
print (singleip)

