#!/usr/bin/python

import os, commands
from py2casefold import casefold

U_STR = raw_input("Enter Text: ")
print casefold(u'U_STR')

#while True:
#    try:
#        U_STR = str(input("Enter Text: "))
#    except:
#        print ("Not a String, Enter words! ")
#    else:
#        print N0,"is a number!"
#        break
