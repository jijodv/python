#!/usr/bin/python

import os, commands



print "Enter 5 Numbers"
N1=input("Number 1: ")
N2=input("Number 2: ")
N3=input("Number 3: ")
N4=input("Number 4: ")
N5=input("Number 5: ")

ARR=[N1, N2, N3, N4, N5]
B_INT=N1
for B_LST in ARR:
	if B_LST > B_INT:
		B_INT = B_LST
		B_ARR_P = ARR.index(B_INT)

print
print"Biggest in the Array is: ", B_INT
print"Position of the biggest number: ", B_ARR_P
print

S_INT=N1
for S_LST in ARR:
	if S_LST < S_INT:
		S_INT = S_LST
		S_ARR_P=ARR.index(S_INT)
print
print"Smallest in the Array is: ", S_INT
print"Position of the smallest number: ", S_ARR_P
print
