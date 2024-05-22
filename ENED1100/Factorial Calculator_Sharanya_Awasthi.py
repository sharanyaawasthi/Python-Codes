# ENED Python 3: Task 3
# File: ACT_Python_3p3_Team375.py
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
# This script is a method to calculate the factorial of a number using the loop function.

numb = int(input('Please enter the number whose factorial is to be found:\n'))
fact = 1

while numb<0:
    print()
    print('Invalid Number Inputted')
    numb = int(input('Please enter the number whose factorial is to be found:\n'))

if numb==0:
    print("The factorial of the inputted number is:\n{0}! = {1}".format(numb,fact))
    
if numb>0:
    for x in range(1,numb+1,1):
        fact = fact*x
    print("The factorial of the inputted number is:\n{0}! = {1}".format(numb,fact))



    
