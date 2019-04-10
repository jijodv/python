#!/usr/bin/python
import os, commands

print
NU = raw_input("Enter Number: ")

FAM=commands.getoutput("cat family.txt").split("\n")
#print type(FAM)
#print FAM

#for F_list in FAM:
for F_list in FAM:
    if NU != F_list.split(",")[0]:
        print
        print "Number Not Found!"
        print
        break
    else:
        REL = F_list.split(",")[1].strip()
        NAME = F_list.split(",")[2].strip()
        print
        print "Name     : ", NAME
        print "Relation : ", REL
        print
        break
