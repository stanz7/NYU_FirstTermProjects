# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 22:47:41 2016

@author: Stanley
"""

inp = input("Please input a line of text:")
letter = input("Please enter the character you want to remove:")
length = len(inp)
hold = -1
for char in inp:
    hold +=1
    if (char == letter):
        inp = inp[:hold]+inp[hold+1:]
        hold -= 1
        
print(inp)