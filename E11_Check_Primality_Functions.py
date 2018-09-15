# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 11: Check Primality functions 
Created on Sat Sep 15 17:08:27 2018

@author: Imaad Shaik
"""
print("This program is to check wether the given number is prime or not")

def get_number():
    return int(input("Enter a number:\n"))

def primality(number):
    j = 0
    for i in range(1, number +  1):
        if number % i == 0:
            j += 1          
        else:
            continue
    return j
        
def print_prime(is_prime):    
    if is_prime == 2:
        print("The entered number is a Prime Number")
    else:
        print("The entered number is a Non-Prime number")
    
number = get_number()
is_prime = primality(number)
print_prime(is_prime)