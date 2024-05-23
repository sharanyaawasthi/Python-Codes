# ENED Python HW 13.2: Task 2
# File: HW13p1_ Task2_awasthsa.py
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
# This program generates random blood pressure systolic values and determines the number of times the
# patient's blood pressure reading was categorized as 'Hypotension', 'Normal' and 'Hypertension'.

import random
nor = 0
hypo = 0
hyper = 0
n = int(input('Please enter the number of BPS readings you wish to take:\n'))

for x in range(1,n+1,1):
    flip = random.randint(50,209)
    if flip>= 50 and flip<90:
        hypo = hypo+1
    elif flip>=90 and flip<120:
        nor = nor+1
    elif flip>=120 and flip<210:
        hyper = hyper+1
print()       
print('The numer of times the BPS was categorized \'Hypotension\':\n',hypo)
print('The numer of times the BPS was categorized \'Normal\':\n',nor)
print('The numer of times the BPS was categorized \'Hypertension\':\n',hyper)



