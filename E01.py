# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 01: Character Input
Created on Tue Sep 11 14:50:47 2018

@author: Imaad Shaik
"""
user_name = input("Please enter your first name:\n")
user_age = input("Please enter your age:\n")
user_age = int(user_age)

age_100 = 2018 + (100 - user_age)

print_times = input("Please enter no. of times the message to be printed:\n")
print_times = int(print_times)

for i in range(print_times):
        print("Hi, " + user_name + ". You will be 100 years old at " + str(age_100))