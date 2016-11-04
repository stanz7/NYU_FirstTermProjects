# -*- coding: utf-8 -*-
"""
Created on Wed Oct  5 15:41:16 2016

@author: Stanley
"""

n= int(input('PLease enter n: '))

#version 1
for line_num in range(1, n+1):
    curr_line = ' ' * *n-line_num) * '*'* line_num
    print(curr_line)
    
print()
print()

#version 2

num_stars = 1
num_spaces = n - 1
for line_num in range(1,n+1):
    curr_line =' ' * num_spaces + "*" *  num_stars
    print(curr_line)
    num_stars +=1
    num_spaces -= 1