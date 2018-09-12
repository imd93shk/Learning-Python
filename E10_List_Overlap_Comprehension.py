# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 10: List overlap comprehension 
Created on Wed Sep 12 20:40:24 2018

@author: Imaad Shaik
"""
import random

size_list_a = int(input("Enter the size of 1st list\n"))
size_list_b = int(input("Enter the size of 2nd list\n"))
range_list = int(input("Enter the range of the numbers\n"))

list_a = random.sample(range(range_list), size_list_a)
list_b = random.sample(range(range_list), size_list_b)

list_comp = [i for i in set(list_a) if i in list_b]

list_a_str = [str(x) for x in list_a]
list_b_str = [str(y) for y in list_b]
list_comp_str = [str(z) for z in list_comp]

print("In the randomly generated lists of numbers", ", ".join(list_a_str), "and",", ".join(list_b_str), "\nThese are the common numbers", ", ".join(list_comp_str))