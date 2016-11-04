# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 13:10:36 2016

@author: Stanley
"""

from random import randint
n = int(input("Enter how many coin flips:"))
h = 0
t = 0



while (n > 0):
    rand = randint(0,2)
    if (rand == 0):
        print ("Heads")
        h += 1
        n -= 1
    if (rand == 1):
        print ("Tails")
        t += 1
        n -= 1
print (" You got ", h, "Heads and", t, "Tails!! Andrew. The probability of heads:tails in this trial is", h, ":", t)
        
    

