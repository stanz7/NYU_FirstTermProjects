# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:45:36 2016

@author: Stanley
"""
import turtle

print ('Please enter the length of the 2 kgs of a right triangle')
side1 = int(input('side 1:'))
side2 = int(input('side 2:'))
c =( (side1 * side1) + (side2 * side2) ) ** 0.5


turtle.forward(side1)
turtle.left(90)

turtle.forward(side2)
turtle.left(150)

turtle.forward(c)

