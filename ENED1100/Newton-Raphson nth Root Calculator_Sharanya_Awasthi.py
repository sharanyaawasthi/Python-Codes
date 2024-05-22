# ENED Python 3: Task 4
# File: ACT_Python_3p4_Team375.py
# Date: 11/16/2023
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
# DESCRIPTION OF THE PROGRAM
# This script is a method to estimate the nth root of a number using the Newton Raphson method.
# The Newton-Raphson method allows to determine the required root using basic calculations.

N = int(input('Please enter the number whose nth root is to be found:\n'))
n = int(input('Please enter the root:\n'))
tol = float(input('Please enter the tolerance:\n'))
est = int(input('Please enter the initial estimate of the root:\n'))

iterations = 0
error = abs((est**n)-N)

while error>tol:
    estpre = est
    est = est - (((est**n)-N)/(n*(est**(n-1))))
    error = abs(est-estpre)
    iterations = iterations+1

print("The Estimate for {0}th root of {1:.2f} = {2:.6f}".format(n,N,est))
print('The number of iterations are:',iterations)




    
