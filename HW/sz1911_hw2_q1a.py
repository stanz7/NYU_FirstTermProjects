# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 12:13:21 2016

@author: Stanley
"""

"""
#1
"""
    
wt = float(input("Please enter your weight in kilograms:"))
ht = float(input("Please enter your height in meters:"))

BMI = wt/(ht*ht)
print (BMI)

a = float(input("Please enter your weight in pounds:"))
b = float(input("Please enter your height in inches:"))

cwt = a*.453592
cht = b*.0254
cBMI = cwt/(cht*cht)
print (cBMI)
