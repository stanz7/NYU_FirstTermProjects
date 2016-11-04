# -*- coding: utf-8 -*-
"""
Created on Wed Oct 12 19:16:04 2016

@author: Stanley
"""

n = int(input("Please input a positive integer, n:"))
holder = n
n_inverse = 0

while (n >= 0):
    space_num =  (holder - n)
    print (" "* space_num + "*" * (2*n - 1) )
    n -= 1
    n_inverse += 1
    if (n_inverse == holder):
        while (n_inverse >= 0):
            y = (holder-(holder-n_inverse))
            print (" "* y + "*" * (holder - n_inverse)+ "*" * (holder-n_inverse -1))
            n_inverse -= 1
    

    
