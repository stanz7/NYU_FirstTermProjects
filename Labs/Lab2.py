# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 11:21:32 2016

@author: Stanley
"""
import math
import turtle

'''
Question 1
'''
val = int(input('Please enter an integer for Kg amount:'))

pounds = (val * 2.2046 )
oz = (val * 16)

print (val, 'kilograms is', pounds, 'pounds and', oz,'ounces')

'''
Question 2
'''
days = int(input('Please input the amount of  days:'))
week = (days//7)
day = (days%7)
print (days, 'is', week, 'weeks and', day, 'days')

'''
Question 3
'''
rad = int(input('Please input radius:'))
c = 2 * rad * math.pi
area = math.pi * (rad**2)
print ('Circumference of the circle is', c, 'and area of the circle is', area)

'''
Question 4
'''
hexagon = turtle.Turtle()
hexagon.forward(100)
hexagon.right(60)
hexagon.forward(100)
hexagon.right(60)
hexagon.forward(100)
hexagon.right(60)
hexagon.forward(100)
hexagon.right(60)
hexagon.forward(100)
hexagon.right(60)
hexagon.forward(100)
hexagon.right(60)
turtle.done()