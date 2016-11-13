# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:23:32 2016

@author: ezhu2
"""

word = str(input("Enter word"))
vowels = 0
cosonants = 0
for i in word:
    if (ord(i) == 65) or (ord(i) == 69) or (ord(i) == 73) or (ord(i) == 79) or (ord(i) == 85) or (ord(i) ==  97) or (ord(i) == 101) or (ord(i) ==  105)or (ord(i) == 111) or (ord(i) == (117)):        
            
       vowels += 1
    else: 
        cosonants += 1
print("Amount of vowels is",vowels,)
print("Amount of cosonants is" ,cosonants)
