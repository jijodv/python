#!/usr/bin/python -x

import os, commands



print "Enter 5 Numbers"
N0=raw_input("Number 0: ")
N1=raw_input("Number 1: ")
N2=raw_input("Number 2: ")
N3=raw_input("Number 3: ")
N4=raw_input("Number 4: ")

#print type(N0)
#if type(N0) is not int:
#	print "One of the input is not Number!"
#	exit()

ARR=[N0, N1, N2, N3, N4]
B_INT=N0
for B_LST in ARR:
	if B_LST > B_INT:
		B_INT = B_LST
		B_ARR_P = ARR.index(B_INT)

S_INT=N0
for S_LST in ARR:
	if S_LST < S_INT:
		S_INT = S_LST
		S_ARR_P = ARR.index(S_INT)

print
print"Biggest in the Array is: ",B_INT
print"Position of the biggest number: ",B_ARR_P
print
print"Smallest in the Array is: ",S_INT
print"Position of the smallest number: ",S_ARR_P
print
