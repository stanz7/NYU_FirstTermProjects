# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:38:10 2016

@author: Stanley
"""

inp = input("Please input a string containing only lowercase letters:")
alpha = "abcdefghijklmnopqrstuvwxyz"
length = len(inp)
flag = True
counter = 0


while (length > 0):
    if (length != 1):
        if (alpha.index(inp[counter]) > alpha.index(inp[counter + 1])):
            flag = False
    length -= 1
    counter +=1
    
if (flag == True):
    print (inp,"is increasing")
else:
    print (inp,"is not increasing")