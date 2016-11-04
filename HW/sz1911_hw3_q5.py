# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:32:30 2016

@author: Stanley
"""
import math

print ("Please enter the length of the a triangle's sides:")
a = int(input("Length of the first side:"))
b = int(input("Length of the second side:"))
c = int(input("Length of the third side:"))

if (a == b == c):
    print (a, b, c, "form an equilateral triangle.")
if (((a == b) and (a != c)) | ((b == c) and (b != a))):
    if ((a==b) and (a != c)):
        if (c == (a * math.sqrt(2))):
            print (a, b, c, "form an isoceles right triangle.")
        print (a,b,c, "form an isoceles triangle")
    if ((b==c) and (b != a)):
        if (a == (b * math.sqrt(2))):
            print (a, b, c, "form an isoceles right triangle.")
        print (a,b,c, "form an isoceles triangle")

print ("This triangle is not isoceles or equilateral")