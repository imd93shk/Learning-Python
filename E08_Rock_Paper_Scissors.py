# -*- coding: utf-8 -*-
"""
www.practicepython.org
Exercise 08: Rock Paper Scissors 
Created on Tue Sep 11 22:46:57 2018

@author: Imaad Shaik
"""
print("This program is a game of Rock Paper Scissors for 2 players")

def play_again():
    play_again = input("If you want to play again, press Y else press N\n")
    if play_again == "Y":
        game_rules()
    else:
        return  

def game_rules():
    p1 = input("Player 1, please type one of the following: Rock, Paper or Scissor\n")
    
    p2 = input("Player 2, please type one of the following: Rock, Paper or Scissor\n")
    
    if ((p1 == "Rock" or p1 == "rock") or (p1 == "Paper" or p1 == "paper") or (p1 == "Scissor" or p1 == "scissor")) and \
       ((p2 == "Rock" or p2 == "rock") or (p2 == "Paper" or p2 == "paper") or (p2 == "Scissor" or p2 == "scissor")):
        if (p2 == "Rock" or p2 == "rock") and (p1 == "Paper" or p1 == "paper"):
            print("\nPaper beats Rock. Player 1 WINS")
            play_again()
        elif (p2 == "Paper" or p2 == "paper") and (p1 == "Scissor" or p1 == "scissor"):
            print("\nScissor beats Rock. Player 1 WINS")
            play_again()
        elif (p1 == "Rock" or p1 == "rock") and (p2 == "Scissor" or p2 == "scissor"):
            print("\nRock beats Scissor. Player 1 WINS")
            play_again()
        elif ((p1 == "Rock" or p1 == "rock") and (p2 == "Rock" or p2 == "rock")) or \
             ((p1 == "Paper" or p1 == "paper") and (p2 == "Paper" or p2 == "paper")) or \
             ((p1 == "Scissor" or p1 == "scissor") and (p2 == "Scissor" or p2 == "scissor")):
            print("\nIt's a DRAW")  
            play_again()
        else:
            print("\nPlayer 2 WINS")
            play_again()
    else:
        print("\nInput Error: You have not selected Rock, Paper or Scissor")
        play_again()
    
game_rules()
