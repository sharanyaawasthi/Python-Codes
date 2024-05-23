# ENED Python HW 13.2: Task 3
# File: HW13p1_Task3_awasthsa.py
# Date: 11/28/2023
# By: Sharanya Awasthi
# Section: 022
# Team: 375
#
# ELECTRONIC SIGNATURE
# Sharanya Awasthi
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
# 
# This program displays the prime and perfect numbers which are less than the number inputted by the user.
# It also gives a count of how many prime and perfect numbers exist below the number given by the user.

import math
c1 = 0
c2 = 0 
k = int(input("Please enter a number:\n"))
print()
for w in range(2,k,1):
    S = 0
    n = w
    m = math.ceil(n/2)+1
    for p in range(2,m,1):
        R = n%p
        if R==0:
            S=S+p
    if S==0:
        print('The number n = {0} is Prime'.format(n))
        c1 = c1+1
    elif S==n-1:
        print('The number n = {0} is Perfect'.format(n))
        c2=c2+1
print()
print('The total number of prime numbers found is {0}'.format(c1))
print('The total number of perfect numbers found is {0}'.format(c2))

        
