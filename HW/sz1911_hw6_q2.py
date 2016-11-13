# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 20:47:36 2016

@author: Stanley
"""

##2

odds = input("Please enter an odd length string:")
length = len(odds)
half = (length//2) 

print(odds[half])
print(odds[0: half])
print(odds[half + 1: length])