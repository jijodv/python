#!/usr/bin/python

###
## Find the Big & Small numbers with its position in Array.
###

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
print"Position of Smallest number in array is: ", S_P
print
print "Sequence you've keyed in: ",ARR
print
print "Swapping positions of these Big & Small Number..."
ARR[B_P], ARR[S_P] = ARR[S_P], ARR[B_P]
print
print "Positions after Swapping: ",ARR

B_N=max(ARR)
B_P=ARR.index(B_N)
S_N=min(ARR)
S_P=ARR.index(S_N)

print
print"Biggest number in the array is: ", B_N
print"New Position of Biggest number in array is: ", B_P
print
print"Smallest number in the array is: ", S_N
print"New Position of Smallest number in array is: ", S_P
print
