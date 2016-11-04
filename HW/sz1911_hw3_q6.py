# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:55:16 2016

@author: Stanley
"""
import turtle
import math
a = int(input("Please enter the length of side a:"))
b = int(input("Please enter the length of side b:"))
angle = int(input("Please enter the angle measure between a and b:"))
c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(angle))
angle2 = math.cos((c**2 + b**2 - a**2)/(2*a*b))
triangle = turtle.Turtle()  
triangle.forward(a)
triangle.left(180-angle)
triangle.forward(b)
triangle.left(angle2)
triangle.forward(c)
