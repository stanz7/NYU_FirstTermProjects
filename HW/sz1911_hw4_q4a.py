# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:40:54 2016

@author: Stanley
"""

length = int(input("Please enter the length of the sequence:"))
holder = length
geomean = 1
while (length > 0):
    input_val = int(input())
    geomean *= input_val
    length -= 1
geomean = (geomean ** (1/holder))
print (geomean)