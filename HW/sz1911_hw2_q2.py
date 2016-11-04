# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 12:13:21 2016

@author: Stanley
"""

"""
#2
"""
print ("Please enter amount of coins:")
q = int(input("Please enter the number of quarters:"))
d = int(input("Please enter the number of dimes:"))
n = int(input("Please enter the number of nickels:"))
p = int(input("Please enter the number of pennies:"))

total = (q*25) + (d*10) + (n*5) + (p*1)
dollars = (total//100)
cents = (total%100)

print ("You have", dollars, "dollars and", cents, "cents")
