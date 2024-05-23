# ENED1120 Python HW: Task 2
# File: HW2p1_Task2_awasthsa.py
# Date: 01/23/2024
# By: Sharanya Awasthi
# Section: 016
# Team: 282
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
# This program inputs a number (N) from the user and lists down all the numbers 'n' (1<=n<=N)
# while also printing whether the number is a happy number, a perfect number, a narcissistic number,
# a combination of them or neither of the three. 

####################################################################
def Happy(num):
    count=0
    while num != 1 and count<100:
        count=count+1
        num0=0
        for digit in str(num):
            num0 = num0+(int(digit))**2
            num = num0
    return num == 1
#####################################################################
def Perfect(num):
    divisors = 0
    for i in range(1,num):
        if num % i == 0:
            divisors = divisors +i
    return divisors == num
######################################################################
def Narcissistic(num):
    narcis=0
    num_str = str(num)
    num_digits = len(num_str)
    for digit in num_str:
        narcis = narcis+(int(digit))**num_digits
        
    return narcis == num
######################################################################
##############Start your script here################################

N = int(input('Please enter a whole number:\n'))
while N<=0:
    print()
    print('Invalid Number Entered')
    N = int(input('Please enter a whole number:\n'))
list1 = []
numtype = []
for x in range (1,N+1):
    list1.append(x)
    if Happy(x)==True:
        Ntype = 'h'
    else:
        Ntype = ''
    if Perfect(x)==True:
        Ntype = Ntype + 'p'
    else:
        pass
    if Narcissistic(x)==True:
        Ntype = Ntype + 'n'
    else:
        pass
    numtype.append(Ntype)
    
for m in range(len(numtype)):
    if numtype[m]=='':
        numtype[m] = 'neither \'h\', \'p\' nor \'n\''
    else:
        pass
print()
for q in range (N):
    print('{0} is {1}\n'.format(list1[q],numtype[q]))
    
        

    
    




















           
        
        


        
    

    
              
    
    
    
    
