# ENED Python HW 10.2: Task 2
# File: HW_10p2_Task2_awasthsa.py
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
# This program calculates the velocity of the roller coaster at point 2 given the speed of the roller coaster (m/s),
# friction coefficient, distance travelled (m), initial elevation (m) and the final elevation (m).

v1 = float(input('Enter the roller coaster speed (m/s):\n'))
f = float(input('Enter the friction coefficient:\n'))
d = float(input('Enter the distance travelled (m):\n'))
y1 = float(input('Enter the initial elevation (m):\n'))
y2 = float(input('Enter the final elevation (m):\n'))

v2 = ((v1**2)-((f*d)*9.81)+((y1-y2)*9.81)*2)**(1/2)
print()
print("The Value of v2 = {0:.2f} m/s".format(v2))

