# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 21:09:07 2016

@author: Stanley
"""

##nonstring method
inp = input("Please enter a 1-length char:")
lowerc = "abcdefghijklnopqrstuvwxyz"
upperc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
char = "1234567890"

if (inp in lowerc):
    print(inp,"is a lowercase character.")
elif (inp in upperc):
    print(inp,"is an uppercase character.")
elif (inp in char):
    print(inp,"is a numeric character.")
else:
    print(inp,"is a non-alphanumeric character.")
    
##string method

inpt = input("Please enter a 1-length char:")

if (inpt.islower()):
    print(inpt,"is a lowercase character.")
elif (inpt.isupper()):
    print(inpt,"is an uppercase character.")
elif (inpt.isnumeric()):
    print(inpt,"is a numeric character.")
else:
    print(inpt,"is a non-alphanumeric character.")