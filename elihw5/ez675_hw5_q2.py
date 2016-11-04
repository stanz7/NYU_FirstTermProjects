# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 20:09:19 2016

@author: ezhu2
"""

n= int(input("Enter size of pyramid"))
for i in range(n):
    print(" "*(n-i + 1),end="" )
    j = 0
    while j<=i:
        print((j+1),end ="")
        j+=1
    print()
