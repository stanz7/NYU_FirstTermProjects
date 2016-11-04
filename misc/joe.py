# -*- coding: utf-8 -*-
"""
Created on Wed Oct 19 22:17:55 2016

@author: Stanley
"""

num = int(input("Input a number:"))

while (num > 0):
    if (num >= 10):
        print ("*" * 10)
    num -=1
    print ("*")
