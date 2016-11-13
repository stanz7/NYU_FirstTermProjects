# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 01:27:49 2016

@author: Stanley
"""

password = str(input("Please enter a password:"))
upper = 0
lower = 0
special = 0
digit = 0

for i in password:
    if i.isdigit():
        digit += 1
    elif i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    else:
        special += 1

if (upper >= 2) and (lower >= 1) and (digit >= 2) and (special >= 1):
    print(password,"is a valid password.")
else:
    print(password,"is an invalid password.")