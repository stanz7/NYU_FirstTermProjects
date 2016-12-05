# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:58:45 2016

@author: Stanley
"""

shift = int(input("Enter right shift amount:"))
string = str(input("Enter string with at least one capital letter:"))
shifted_string = ""
for i in string:
    if i.isalpha():
        if i.isupper():
            if ord(i)+shift > 90:
                shifted_string += chr(65 + abs(91 -(ord(i)+shift)))
            elif ord(i)+shift < 90 and (ord(i)+shift) >= 65:
                shifted_string += chr(ord(i)+shift)
        if i.islower():
            if ord(i) + shift > 122:
                shifted_string += chr(97+ abs(123 - (ord(i)+shift)))
            else:
                shifted_string += chr(ord(i)+shift)
    elif i == " ":
        shifted_string += " "
    elif i.isdigit():
        shifted_string += i
    elif i == "!":
        shifted_string+= "!"
    else:
        shifted_string += i

print(shifted_string)