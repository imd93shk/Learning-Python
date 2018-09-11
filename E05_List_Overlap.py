# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 05: List overlap
Created on Tue Sep 11 16:24:51 2018

@author: Imaad Shaik
"""
print("This program is used to print out a common list of values from the given two lists of numbers")
list_a = [int(x) for x in input("Please enter your first number list\n").split(",")]
list_b = [int(x) for x in input("Please enter your second number list\n").split(",")]

#print(list_a)
#print(list_b)

common_list = [] 

for x in list_a:
    for y in list_b:
        if x == y:
            common_list.append(x)
        else:
            continue

common_list_non_repeated = list(set(common_list))
common_list_non_repeated_str = [str(x) for x in common_list_non_repeated]
print("\nThe common numbers in the entered two lists are:\n" + ", ".join(common_list_non_repeated_str))