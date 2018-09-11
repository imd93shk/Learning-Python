# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 07: List Comprehensions
Created on Tue Sep 11 22:35:05 2018

@author: Imaad Shaik
"""
print("This program is to get new list of even number from the given number using List Comprehensions")
list_a = [int(x) for x in input("Enter the list of numbers seperated by commas\n").split(",")]

even_list = [x for x in list_a if x % 2 == 0] 
print(even_list)