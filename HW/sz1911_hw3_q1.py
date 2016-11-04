# -*- coding: utf-8 -*-
"""
Created on Mon Oct  3 16:07:53 2016

@author: Stanley
"""

wt = float(input("Please enter your weight in kilograms:"))
ht = float(input("Please enter your height in meters:"))

BMI = wt/(ht*ht)
if (BMI < 18.5):
    print (BMI, "Weight Status: Underweight")
if (18.5 <= BMI <= 24.9):
    print (BMI, "Weight Status: Normal")
if (25.0 <= BMI <= 29.9):
    print (BMI, "Weight Status: Overweight")
if (30.0 <= BMI):
    print (BMI, "Weight Status: Obese")
    
a = float(input("Please enter your weight in pounds:"))
b = float(input("Please enter your height in inches:"))

cwt = a*.453592
cht = b*.0254
cBMI = cwt/(cht*cht)
if (cBMI < 18.5):
    print (cBMI, "Weight Status: Underweight")
if (18.5 <= cBMI <= 24.9):
    print (cBMI, "Weight Status: Normal")
if (25.0 <= BMI <= 29.9):
    print (cBMI, "Weight Status: Overweight")
if (30.0 <= BMI):
    print (cBMI, "Weight Status: Obese")
