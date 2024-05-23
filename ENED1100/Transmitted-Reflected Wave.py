# ENED Python HW 10.2: Task 3
# File: HW_10p2_Task3_awasthsa.py
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
# This program calculates the angle of the transmitted wave (Degrees),
# Amplitude of the Reflected Wave (V/m) and, the Amplitude of the Transmitted Wave (V/m) given
# the Amplitude of the incident wave (V/m), intrinsic impedance of material 1 (ohms),
# Enter the intrinsic impedance of material 2 (ohms), angle of incidence (In Degrees),
# the refractive index of medium 1 and the refractive index of medium 2.

import math
AMPi = float(input('Enter the amplitude of the incident wave(V/m):\n'))
INT1 = float(input('Enter the intrinsic impedance of material 1 (ohms):\n'))
INT2 = float(input('Enter the intrinsic impedance of material 2 (ohms):\n'))
ANGLEi = float(input('Enter the angle of incidence (In Degrees):\n'))
ANGLEiRAD = (math.pi/180)*ANGLEi
n1 = float(input('Enter the refractive index of medium 1:\n'))
n2 = float(input('Enter the refractive index of medium 2:\n'))

ANGLEt = math.asin((n1*math.sin(ANGLEiRAD))/n2)
ANGLEtDeg = ANGLEt*(180/math.pi) 

AMPr = ((INT2*math.cos(ANGLEiRAD))-(INT1*math.cos(ANGLEt)))/((INT2*math.cos(ANGLEiRAD))+(INT1*math.cos(ANGLEt)))*AMPi
AMPt = ((2*INT2*math.cos(ANGLEiRAD))/((INT2*math.cos(ANGLEt))+(INT1*math.cos(ANGLEiRAD))))*AMPi
unit1 = 'Degrees'
unit2 = 'V/m'
print()
print('The angle of the transmitted wave is:\n{0:0.2f} {1}'.format(ANGLEtDeg,unit1))
print('The Amplitude of the Reflected Wave is:\n{0:0.2f} {1}'.format(AMPr,unit2))
print('The Amplitude of the Transmitted Wave is:\n{0:0.2f} {1}'.format(AMPt,unit2))
