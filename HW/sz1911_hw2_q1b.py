# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 18:05:45 2016

@author: Stanley
"""

"""
#1b
"""
a = float(input("Please enter your weight in pounds:"))
b = float(input("Please enter your height in inches:"))

cwt = a*.453592
cht = b*.0254
cBMI = cwt/(cht*cht)
print (cBMI)