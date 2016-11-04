# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:58:59 2016

@author: Stanley
"""

n = int(input("Enter input n:"))

for i in range(n):
    print(" "*(n-i), end="")
    m = 0
    while m<=i:
        print((m+1),end="")
        m+=1
    print()