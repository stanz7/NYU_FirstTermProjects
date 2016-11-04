# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 20:45:25 2016

@author: Stanley
"""

print ("Please enter a non-empty sequence of positive integers, each one in a seperate line. End your sequence by typing done.")
geomean = 1
length = 0
while (input != "done"):
    try:
        num = int(input())
        geomean = geomean * num
        length +=1
    except ValueError:
        print (geomean ** (1/length))
    
    
    
    