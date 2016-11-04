# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 15:31:39 2016

@author: Stanley

"""

import turtle
print ('Please enter the length of the side of your square')
side = int(input())

turtle.forward(side)
turtle.left(90)

turtle.forward(side)
turtle.left(90)

turtle.forward(side)
turtle.left(90)

turtle.forward(side)
turtle.left(90)

turtle.hideturtle()

turtle.done()