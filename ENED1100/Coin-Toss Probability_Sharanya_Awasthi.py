# ENED Python 3: Task 2
# File: ACT_Python_3p2_Team375.py
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
# This script is a method to stimulate a probability problem that invloves
# fliping a coin. Using this program the user can find the probability of
# getting a heads or a tail while flipping a coin.

import random

coin = int(input('Please enter the number of times to flip the coin:\n'))
h=0
t=0

for x in range(coin):
    flip=random.randint(0,1)
    if flip==0:
        t=t+1
    else:
        h=h+1

print('The number of tails counted: ',t)
print('The number of heads counted: ',h)
print()
tpercent = (t/coin)*100
hpercent = (h/coin)*100

print('The percentage of flips which were tails: {0:0.2f}'.format(tpercent))
print('The percentage of flips which were heads: {0:0.2f}'.format(hpercent))
      

