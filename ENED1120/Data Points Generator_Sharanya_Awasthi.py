# ENED1120 Python HW: Task 1
# File: HW2p1_Task1_awasthsa.py
# Date: 01/20/2024
# By: Sharanya Awasthi
# Section: 016
# Team: 282
#
# ELECTRONIC SIGNATURE
# Sharanya Awasthi
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
# DESCRIPTION OF THE PROGRAM
# This program creates a function which generates data points based on user input and sorts the data
# values into bins of equal width. It then stores the frequency distribution of the
# data points in a list and prints the list.

import math

def HW2p1_Task1_awasthsa(a,b,N):
    X = [0.1]
    Y = [0.2]
    FD = []
    for i in range (0,N-1):
        y = (-b*X[i])+(a*Y[i])-((Y[i])**3)
        Y.append(y)
        x = Y[i]
        X.append(x)
    bins = 1 + (math.ceil(math.log2(N)))
    width = (max(X)- min(X))/bins
    Z = [min(X)]
    for w in range(1,bins+1):
        z = Z[w-1]+width
        Z.append(z)
    for m in range(len(Z)-1):
        c1 = 0
        for q in range(len(X)):
            term = X[q]
            if term>=Z[m] and term<Z[m+1]:
                c1 = c1+1
            else:
                c1 = c1+0
        FD.append(c1)
    FDLEN = len(FD)
    FD[(len(FD))-1] = FD[(len(FD))-1]+1
    print('The Frequency Distribution is:')
    return FD

