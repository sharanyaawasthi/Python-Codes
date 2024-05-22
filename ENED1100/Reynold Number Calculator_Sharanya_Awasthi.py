# Activity Python 1: Task 3
# File: ACT_Python_1p3_Team375.py
# Date: 10/26/2023
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
# This program calculates the Reynold's Number using the inputs from the user.
# The user inputs the Fluid Velocity in (mph), the Typical Length in (in), the Dynamic Viscosity in (lb/(in*s)) and the density of fluid in (lb/in^3) 
print('Reynold Number Calculator')
print()
V = float(input('Please enter the Fluid Velocity in (mi/hr):\n'))
V1 = V/2.237
L = float(input('Please enter the Typical Length in (in):\n'))
L1 = L/39.37
u = float(input('Please enter the Dynamic Viscosity of the fluid in (lb/(in*s):\n'))
u1 = u*17.8579673
p = float(input('Please enter the Density of the Fluid in (lb/in^3):\n'))
p1 = p*27679.9

Re = (p1*V1*L1)/u1
print()
print('The Reynolds Number (Re) is calculated to be:\n{0:0.2f}'.format(Re))
