# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 04: Divisor
Created on Tue Sep 11 16:11:34 2018

@author: Imaad Shaik
"""
print("This program is used for finding all the divisor of a given number")
number = input("Please enter a number: \n")
number = int(number)

all_num_btwn_number = range(1, number+1)
divisors = []
for x in all_num_btwn_number:
    if number % x == 0:
        divisors.append(x)  
    
print("These are the numbers which divide the given number " + str(number) + " evenly:")
divisors_str = [str(x) for x in divisors]
print(", ".join(divisors_str))
