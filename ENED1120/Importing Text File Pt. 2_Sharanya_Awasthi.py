# ENED1120 Python HW: Task 2
# File: HW3p2_Task2_awasthsa.py
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
# This program browses a file which contains a list of questions and the prompts the user
# to enter a random number to add that many random questions into a new file. The user
# decides whether to store a question or not.

import random
n = int(input("How many questions to store in a new file? "))
x = open('TeamQuestion.txt', 'r')
questions = x.readlines()
x.close()
questionlist = []
for i in range(n):
    answer = "n"
    while(answer=="n"):
        r = random.randint(0, len(questions))
        print(questions[r])
        answer = input("Keep this question? (Enter y or n): ")
        if(answer=="y"):
            questionlist.append(questions[r])
y = open("QuestionsToAsk.txt", "w")
for j in questionlist:
    y.write(j)
y.close()
