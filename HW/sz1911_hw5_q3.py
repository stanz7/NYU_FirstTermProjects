# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 23:28:54 2016

@author: Stanley
"""

n = int(input("Please enter input:"))

for i in range(1,n+1):
    if(i%2==0) and (i<10):
        print(i)
    else:
        num = i
        even = 0
        odd = 0
        if(num%2==0):
            even +=1 
            num = num//10
        if(num%2==1):
            odd += 1
            num = num//10
        elif(even>odd):
            print(i)
            
        