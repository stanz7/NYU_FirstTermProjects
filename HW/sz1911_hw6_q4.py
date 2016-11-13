# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 01:04:13 2016

@author: Stanley
"""

##4

inp = input("Enter a mathematical expression:")
ind = inp.index(" ") + 1

for i in range(0, len(inp)):
    if inp[i] == " ":
        numa = inp[0: i]
        symbol = inp[i + 1]
        numb = inp[i+2: len(inp)]
        break

if (symbol == "+"):
    result = int(numa) + int(numb)
    print(result)
elif (symbol == "*"):
    result = int(numa) * int(numb)
    print(result)
elif (symbol == "-"):
    result = int(numa) - int(numb)
    print(result)
elif (symbol == "/"):
    result = int(numa)/int(numb)
    print(result)
        
