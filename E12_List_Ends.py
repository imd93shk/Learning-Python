# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 12: List Ends
Created on Sat Sep 15 17:43:01 2018

@author: Imaad Shaik
"""
print("This program takes a list of numbers and makes a new list of only the first and last elements of the given list")

def list_num():
    list_num = [int(x) for x in input("Enter a list of numbers seperated by commas:\n").split(",")]
    return list_num
    
def new_list(list_num):
    new_list = [list_num[x] for x in range(len(list_num)) if x == 0 or x == len(list_num) -1 ]
    return new_list

def list_str(list):
    return [str(x) for x in new_list]

list_num = list_num()
new_list = new_list(list_num)
new_list_str = list_str(new_list)

print("First and last numbers of the list are" , ", ".join(new_list_str))