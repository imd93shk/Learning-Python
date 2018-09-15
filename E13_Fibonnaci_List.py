# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 13: Fibonnaci List 
Created on Sat Sep 15 19:02:18 2018

@author: Imaad Shaik
"""
def get_numbers():
    number = int(input("Enter how many Fibonnaci numbers do you want to generate\n"))
    return number

def fibo_gen(number):
    if number > 0:
        if number == 1:
            fibo_list = [1]
        elif number == 2: 
            fibo_list = [1, 1]
        elif number > 2:
            fibo_list = [1, 1]
            for x in range(2, number):
                fibo_list.append(fibo_list[x-1] + fibo_list[x-2])
    else:
        return []
    
    return fibo_list

number = get_numbers()
fibo_list = fibo_gen(number)
fibo_list_str = [str(x) for x in fibo_list]

if number == 1:
    print("The first fibonnaci numbers is " + ", ".join(fibo_list_str))
elif number > 1:    
    print("The first", number, "fibonnaci numbers are " + ", ".join(fibo_list_str))
else:
    print("Error: Number is invalid or negative")