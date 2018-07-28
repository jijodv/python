#!/usr/bin/python

###
## Find the Big & Small numbers with its position in Array.
###

import os, commands

print
print "Enter 5 Numbers"
N0=input("Number 0: ")
N1=input("Number 1: ")
N2=input("Number 2: ")
N3=input("Number 3: ")
N4=input("Number 4: ")


ARR=[N0, N1, N2, N3, N4]
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
