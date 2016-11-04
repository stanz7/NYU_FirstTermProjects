# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 21:50:31 2016

@author: ezhu2
"""

n = int(input("Enter number"))
for i in range(1,n+1):
    if (i % 2 == 0) and (i <= 9):
        print (i)
    else:
        num = i
        even = 0
        odd = 0
        if (num % 2 == 0):
            even += 1
            num = num//10
        if(num % 2 == 1):
            odd += 1
            num = num//10
        elif even > odd:
            print(i)
            
    
    