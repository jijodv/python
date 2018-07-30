#!/usr/bin/python

import os, commands

while True:
    try:
        U_STR=str(raw_input("Enter Text: "))
    except:
        print ("Not a String, Enter words! ")
    else:
        break
print
LU_STR=U_STR.lower()
R_STR = reversed(LU_STR)
if list(LU_STR) == list(R_STR):
    print "String",U_STR,"is a Palindrome!"
else:
    print "String",U_STR,"is NOT a Palindrome"

print
