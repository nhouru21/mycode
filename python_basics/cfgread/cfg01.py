#!/usr/bin/env python3
######## EXPLORE READ ##########
## create file object in "r"ead mode
configfile = open("vlanconfig.cfg", "r")

## display file to the screen - .read()
print(configfile.read())

## close file
configfile.close()

######## EXPLORE READLINES ##########
## re-create file object to explore new method
configfile = open("vlanconfig.cfg", "r")

## make a list of file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

## Iterate through configlist
## Iterate through configlist
for x in configlist:
    print(x.strip())   # by default, .strip will remove any whitespace or newline characters
                       # therefore we no longer want to change "end=" from its default setting of
                       # a newline character

## Always close your file
configfile.close()

