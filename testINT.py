#!/usr/bin/python

import os, commands

while True:
    try:
        N0 = int(input("Enter Number: "))
    except:
        print ("Not an Integer, try again!")
        continue
    else:
        print N0,"is a number!"
        break
