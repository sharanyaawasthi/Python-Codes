# ENED Python HW 11.2: Task 1
# File: HW_11p2_Task1_awasthsa.py
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
# This program outputs the exercise intensity level
# and the calories burned per hour using the input given by the user.

age = float(input("Please enter the user age in years:\n"))
weight = float(input("Please enter the user weight in pounds:\n"))
CHR = float(input("Please enter the user current heart rate in beats/minute:\n"))
m = input("Please enter the type of machine (auto/manual):\n")

if m == "auto" or m == "manual":
    if m == "auto":
        MHR = 206 - (0.88 * age)
        CB = 60 * (((age * 0.2017) + (weight * 0.09036) + (CHR * 0.6309) - 55.0969) / 4.184)
    else:
        MHR = 205.8 - (age * 0.685)
        CB = 60 * (((age * 0.074) - (weight * 0.05741) + (CHR * 0.4472) - 20.4022) / 4.184)

    if CHR < (0.6*MHR):
        EIL = "Below Level"
    elif CHR < (0.7*MHR):
        EIL = "Weight Loss"
    elif CHR < (0.8*MHR):
        EIL = "Cardio"
    elif CHR < (0.9*MHR):
        EIL = "Anaerobic (Hardcore)"
    else:
        EIL = "Above Level"
    print()
    print('Calories burnt per hour is: {0:.2f}, for an activity level of: {1}'.format(CB, EIL))

else:
    print()
    print("Invalid")
