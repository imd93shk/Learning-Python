# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 03: List Less Than Ten
Created on Tue Sep 11 15:24:28 2018

@author: Imaad Shaik
"""
print("This program will take 10 numbers from the user (each seperated by a comma) and display numbers less than 5")
def input_10_val():
    number = [int(x) for x in input("Please enter 10 numbers (each seperated by a comma)\n").split(",")]
    return number

def less_5_calculation():
    number = input_10_val()
    if len(number) < 10:
        print("\nError: Entered numbers are less than 10")
        less_5_calculation()
    elif len(number) > 10:
        print("\nError: Entered numbers are more than 10")
        less_5_calculation()
    else:
        entered_num = [str(x) for x in number]
        print("\nEntered numbers are " + ", ".join(entered_num))
        less_5 = []
        for i in range(len(number)):
            if number[i] < 5:
                less_5.append(number[i])
            else:
                continue
        less_5_str = [str(x) for x in less_5]
        print("Numbers less than 5 are " + ", ".join(less_5_str))       
            
less_5_calculation()