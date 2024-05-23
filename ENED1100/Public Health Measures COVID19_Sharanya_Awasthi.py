# ENED Python HW 11.2: Task 2
# File: HW_11p2_Task2_awasthsa.py
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
# This program will determine the public health measures to be taken to control the spreading of
# COVID-19 by taking the coefficients sigma, mu, gamma, delta, beta1, beta2 and alpha as inputs from
# the user.

s = float(input("Enter the coefficient sigma: "))
mu = float(input("Enter the coefficient mu: "))
q = float(input("Enter the coefficient gamma: "))
d = float(input("Enter the coefficient delta: "))
b1 = float(input("Enter the coefficient beta1: "))
b2 = float(input("Enter the coefficient beta2: "))
a = float(input("Enter the parameter alpha: "))

F = ((d * (b1 * s)) + ((q + mu) * b2)) / ((s + mu) * (q + mu) * mu)
R = (1 - a) * F
ac = 1 - (1 / F)

if R == 1:
    if a < ac:
        print()
        print("Endemic state, increase public health measures")
    else:
        print()
        print("No change in public health measures")
else:
    if R > 1:
        if a < ac:
            print()
            print("Disease expansion state, Increase Public Health Measures")
        else:
            print()
            print("No change in public health measures")
    else:
        if a > ac:
            print()
            print("Disease Controlled, Decrease Public Health Measures")
        else:
            print()
            print("No change in public health measures")

