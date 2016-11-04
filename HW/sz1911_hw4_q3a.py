# -*- coding: utf-8 -*-
"""
Created on Thu Oct 13 16:57:34 2016

@author: Stanley
"""

rom_num = (input("Please enter a number in the simplfied Roman System:"))
return_num = 0
counter = 0
length = len(rom_num)
while (length > 0):
    if (rom_num[counter] == "M"):
        return_num += 1000
        counter +=1
        length -= 1
    if (rom_num[counter] == "D"):
        return_num += 500
        counter +=1
        length -= 1
    if (rom_num[counter] == "C"):
        return_num += 100
        counter +=1
        length -= 1
    if (rom_num[counter] == "L"):
        return_num += 50
        counter +=1
        length -= 1
    if (rom_num[counter] == "X"):
        return_num += 10
        counter +=1
        length -= 1
    if (rom_num[counter] == "V"):
        return_num += 5
        counter +=1
        length -= 1
    if (rom_num[counter] == "I"):
        return_num += 1
        counter +=1
        length -= 1
print (return_num)