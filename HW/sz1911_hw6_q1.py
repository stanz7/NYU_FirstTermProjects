# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 19:50:06 2016

@author: Stanley
"""

from random import randint

randnum = randint(0,100)

print("I thought of a number between 1 and 100! Try to guess it!")
n = 6
ranges = 1
rangee = 100


while (n > 0):
    inp = int(input("Please enter your guess:"))
    n -=1
    if (inp > randnum):
        print("Range: [",ranges,",",rangee, "], Number of guesses left =", n )
        print("Your guess:", inp)
        print("Wrong my number is smaller!")
        rangee = inp - 1
    elif (inp < randnum):
        print("Range: [",ranges,",",rangee, "], Number of guesses left =", n )
        print("Your guess:", inp)
        print("Wrong my number is bigger!")
        ranges = inp + 1
    elif (inp == randnum):
        print("Range: [",ranges,",",rangee, "], Number of guesses left =", n )
        print("Your guess:", inp)
        print("Congrats! You got it in ", 6-n, "tries!")
        break
if (n == 0):
    print("Range: [",ranges,",",rangee, "], Number of guesses left =", n )
    print("Your guess:", inp)
    print("Out of guesses! my number was:", randnum)
    
    

    