#!/usr/bin/python

import os, commands

INT=0

print "Enter 5 Numbers"
a=input("Number 1: ")
b=input("Number 2: ")
c=input("Number 3: ")
d=input("Number 4: ")
e=input("Number 5: ")

ARR=[a,b,c,d,e]

for LST in ARR:
	if INT < LST:
		INT = LST
print
print"Biggest in the Array is: ", INT
print

