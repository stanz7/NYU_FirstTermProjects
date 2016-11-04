# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:19:37 2016

@author: Stanley
"""

decimal = int(input("Enter number in decimal form:"))
disp = decimal
return_string = ""
while (decimal != 0):
    if (decimal >= 1000):
        decimal = decimal-1000
        return_string += "M"
    if (500 <= decimal < 1000):
        decimal = decimal-500
        return_string += "D"
    if (100 <= decimal < 500):
        decimal = decimal-100
        return_string += "C"
    if (50 <= decimal < 100):
        decimal = decimal - 50
        return_string += "L"
    if (10 <= decimal < 50):
        decimal = decimal - 10
        return_string += "X"
    if (5 <= decimal < 10):
        decimal = decimal-5
        return_string += "V"
    if (1 <= decimal < 5):
        decimal = decimal -1
        return_string += "I"
    
print (disp, "is", return_string, "in Roman Numeral form")
