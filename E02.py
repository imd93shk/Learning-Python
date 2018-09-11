# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 02: Odd or Even
Created on Tue Sep 11 15:15:19 2018

@author: Imaad Shaik
"""
print("This program is to find whether the given number is even or odd")
number = input("Enter a number: \n")
number = int(number)

if number % 2 == 0 and number % 4 == 0:
    print("The entered number " + str(number) + " is Even and is a multiple of 4")
elif number % 2 == 0 and number % 4 != 0:
    print("The entered number " + str(number) + " is Even")    
else:
    print("The entered number " + str(number) + " is Odd")
    

