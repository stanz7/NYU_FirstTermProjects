# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 01:23:51 2016

@author: Stanley
"""

##5

word = str(input("Enter a word please:"))
vowels = 0
cosonants = 0
for i in word:
    if (ord(i) == 65) or (ord(i) == 69) or (ord(i) == 73) or (ord(i) == 79) or (ord(i) == 85) or (ord(i) ==  97) or (ord(i) == 101) or (ord(i) ==  105)or (ord(i) == 111) or (ord(i) == (117)):        
       vowels += 1
    else: 
        cosonants += 1
print("The amount of vowels is:",vowels,)
print("The amount of cosonants is:" ,cosonants)
