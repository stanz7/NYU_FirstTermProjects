# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:31:43 2016

@author: ezhu2
"""

password = str(input("Enter password"))
special = 0
digits = 0
upper = 0
lower = 0
for i in password:
    print(i)
   
    if i.isdigit() == True:
        digits += 1
    if i.isupper() == True:
        upper += 1
    if i.islower() == True:
        lower += 1
    else:
        special += 1
if (lower >= 1 and upper >= 1) and (digits >=2 and special >= 1):
    print(password ," is a valid password")
else:
    print(password, "is invalid")