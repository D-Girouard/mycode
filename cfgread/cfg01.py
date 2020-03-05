#!/usr/bin/env python3

########## explore read ###############
## cerat file object in "r"ead mode
configfile = open("vlanconfig.cfg","r")

## display file to the screen
print(configfile.read())

## close file
configfile.close()

#####explore readlines#####
## re creat file object to explore new method
configfile = open("vlanconfig.cfg","r")

## meak a list of the file lines 
configlist = configfile.readlines()
print(configlist)

## iterate through configlist
for x in configlist:
    print(x)


#close file
configfile.close()



