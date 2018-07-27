#!/usr/bin/python

###
## Find the Big & Small numbers with its position in Array.
###

import os, commands


print "Enter 5 Numbers"
a=input("Number 0: ")
b=input("Number 1: ")
c=input("Number 2: ")
d=input("Number 3: ")
e=input("Number 4: ")

ARR=[a,b,c,d,e]
B_N=max(ARR)
B_P=ARR.index(B_N)
S_N=min(ARR)
S_P=ARR.index(S_N)

print
print"Biggest number in the array is: ", B_N
print"Position of Biggest number in array is: ", B_P
print
print"Smallest number in the array is: ", S_N
print"Position of Biggest number in array is: ", S_P
print

