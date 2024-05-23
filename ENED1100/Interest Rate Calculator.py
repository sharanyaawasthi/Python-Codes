# ENED Python HW 10.2: Task 1
# File: HW_10p2_Task1_awasthsa.py
# Date: 10/29/2023
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
# This program calculates the Interest Rate, Final Amount and Final Interest Earning
# given the Original Principal Sum, Annual Interest Factor, Compounding Frequency
# & Overall Length of the Interest Period.

import math
print('Interest & Interest Rate Calculator')
#inputs
P = float(input('Please enter the original principal sum value (P):\n'))
print()
x = int(input('Please enter the annual interest factor (x):\n'))
print()
n = int(input('Please enter the compounding frequency (n):\n'))
print()
t = float(input('Please enter the overall length of the interest period (t):\n'))

#Calculations
r = (1/(n**2))*(abs(math.sin(x)/x))
A = P*(1+r)**(n*t)
I = A-P
unit1 = '%'
unit2 = '$'
print()
print()
print('The Interest Rate would be:\n{0:0.4f}{1}\n'.format(r,unit1))
print('The Principal Amount inputted by the user:\n{0}{1:0.2f}\n'.format(unit2,P))
print('The Final Amount would be:\n{0}{1:0.2f}\n'.format(unit2,A))
print('The Final Interest Earning would be:\n{0}{1:0.2f}\n'.format(unit2,I))




