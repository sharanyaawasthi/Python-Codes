# Activity Python 1: Task 5
# File: ACT_Python_1p5B_Team375.py
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
# This program calculates the heat transfer rates in (W) given the temperature
# of the house in (F), Temperature of the air in (F), Surface area of the house
# in (ft^2) and the Height of the house in (ft)

print("Heat Tranfer Rate Calculator")
print()
Thouse = float(input('Please eneter the temperature of the house (F):\n'))
Thouse1 = ((Thouse-32)*(5/9))+273.15
Tair = float(input('Please enter the temperature of the outside air in (F):\n'))
Tair1 = ((Tair-32)*(5/9))+273.15
SArea = float(input('Please enter the surface area of the house in (ft^2):\n'))
SArea1 = SArea*0.09290304
H = float(input('Please enter the Height of the House in (ft):\n'))
H1 = H*0.3048

g = 9.81
B = 1/Tair1

Ra = (g*B*(Thouse1-Tair1)*(H1**3)*0.7)/(1.271e-5**2)

Nu = 0.59*(Ra**0.25)
k = 0.25
HeatTranferCoeff = (k*Nu)/H1

HeatTransferRate = HeatTranferCoeff*SArea1*(Thouse1-Tair1)
Unit = 'W'

print()
print('The Heat Transfer Rate is:\n{0:0.2f}{1}'.format(HeatTransferRate,Unit))

