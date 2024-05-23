# ENED1120 Python HW: Task 1
# File: HW3p2_Task1_awasthsa.py
# Date: 02/01/2024
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
# This program browses the grades of a number of students stored in a text file and
# calculates the letter grade for each student and stores them according to their
# indices in a seperate files. 

x = open('Grades.txt', 'r')
y = x.readlines()
x.close()
data = []
grade = []
letter = []
perc = 0
for i in range(1, len(y)):
    data.append(y[i].split())
for j in range(len(data)):
    for k in range(len(data[j])):
        data[j][k] = float(data[j][k])
for l in range (len(data)):
    grade.append((data[l][1]*0.05)+(data[l][2]*0.15)+(data[l][3]*0.15)+(data[l][4]*0.20)+(data[l][5]*0.45))
for m in grade:
    if(m >= 90):
        letter.append("A")
    elif(m >= 80):
        letter.append("B")
    elif(m >= 70):
        letter.append("C")
    elif(m >= 60):
        letter.append("D")
    elif(m >= 0):
        letter.append("F")
z = open('LetterGrade.txt', 'w')
letterlist = []
letterlist.append("Index"+"    "+"Total"+"    "+"Letter")
for n in range(len(letter)):
    letterlist.append("{0:3}      {1:.2f}      {2}".format(str(n+1), (grade[n]), str(letter[n])))
for o in range(len(letterlist)):
    z.write(letterlist[o]+"\n")
z.close()
