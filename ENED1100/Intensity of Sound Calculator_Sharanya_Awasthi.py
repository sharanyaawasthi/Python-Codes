# Activity Python 1: Task 4
# File: ACT_Python_1p4B_Team375.py
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
# This program calculates the Intensity of Sound in (W/m^2) using the inputs from the user.
# The inputs given by the user are the Maxiumum Allowable SPL in(dB), the reference pressure in (Pa) and the Particle Velocity in (m/s)

print('Intensity Calculator')
print()
SPL = float(input('Please enter a value for the Maximum Allowable SPL in (dB):\n'))
RefP = float(input('Please enter a value for the Reference Pressure in (Pa):\n'))
PVel = float(input('Please enter a value for the Particle Velocity in (m/s):\n'))

P = RefP*(10**(SPL/20))
I = P*PVel
Units = 'W/m^2'
print()
print('The Value of the Intensity is: {0:0.2f} {1}'.format(I,Units))

