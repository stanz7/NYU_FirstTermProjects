# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 01:52:19 2016

@author: Stanley
"""

import math

a = int(input("Please enter the value of a:"))
b = int(input("Please enter the value of b:"))
c = int(input("Please enter the value of c:"))

disc = (b**b)- (4*a*c)
if (disc < 0):
    print ("No Real Solutions")
if (disc == 0):
    print ("Infinite Number of solutions")
if (disc > 0):
    formulaplus = (-b+math.sqrt((b**2)-(4*(a*c))))/(2*a)
    formulaminus = (-b-math.sqrt((b**2)-(4*(a*c))))/(2*a)
    if (formulaplus == formulaminus):
        print ("There is one solution:", formulaplus)
    if (formulaplus != formulaminus):
        print ("There are two solutions:", formulaplus, formulaminus)

