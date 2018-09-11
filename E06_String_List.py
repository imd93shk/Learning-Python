# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 06: String List
Created on Tue Sep 11 22:11:32 2018

@author: Imaad Shaik
"""
print("This program is to check whether the entered string is a Palindrom or not")
entered_str = input("Please enter a desired string\n")
rev_str = entered_str[::-1]

if entered_str == rev_str:
    print("Entered string " + entered_str + " is a Palindrome")
else:
    print("Entered string " + entered_str + " is not a Palindrome")
