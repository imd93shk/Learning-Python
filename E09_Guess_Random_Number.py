# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 09: Guess Random Number
Created on Wed Sep 12 19:01:18 2018

@author: Imaad Shaik
"""
print("This program allow user to guess the random number generated by the program")

import random

play = "Y"
i = 0
old_guess = []

def random_num_gen():
    random_num = random.randint(1, 9)
    return random_num

random_num = random_num_gen()

while play == "Y":
    if i > 0:
        old_guess.append(user_guessed_number)
        old_guess = [str(x) for x in old_guess]
        print("Wrong guesses:", ", ".join(old_guess))
    user_guessed_number = input("Please guess a number between 1 to 9 (both included)\n")
    user_guessed_number = int(user_guessed_number)
    if user_guessed_number == random_num:
        print("Congratulations!!! Your guess", user_guessed_number, "is right!!!")
        print("You guessed the right number in", i+1, "guesses")
    else:
        print("Sorry. Your guess", user_guessed_number, "is wrong.")
        i += 1
    play = input("Do you want to play again? Type Y for Yes and N for No\n")
    

    
