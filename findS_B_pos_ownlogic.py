#!/usr/bin/python -x

import os, commands


print
print "Enter 5 Numbers"
while True:
    try:
        N0 = int(input("Number 0: "))
    except:
        print ("ERROR : Enter Integer in Number 0!")
    else:
        break
while True:
    try:
        N1 = int(input("Number 1: "))
    except:
        print ("ERROR : Enter Integer in Number 1!")
    else:
        break
while True:
    try:
        N2 = int(input("Number 2: "))
    except:
        print ("ERROR : Enter Integer in Number 2!")
    else:
        break
while True:
    try:
        N3 = int(input("Number 3: "))
    except:
        print ("ERROR : Enter Integer in Number 3!")
    else:
        break
while True:
    try:
        N4 = int(input("Number 5: "))
    except:
        print ("ERROR : Enter Integer in Number 4!")
    else:
        break

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
