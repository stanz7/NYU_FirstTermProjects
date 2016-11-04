# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 00:48:04 2016

@author: Stanley
"""

"""
#3
"""

print ("Please enter your amount in the format of dollars and cents in two separate lines:")
d = int(input())
c = int(input())

quarters = ((d*100)//25) + (c//25)
dimes = (((d*100)%25)//10) + ((c%25)//10)
nickels = ((((d*100)%25)%10)//5) + (((c%25)%10)//5)
pennies = (((((d*100)%25)%10)%5)//1) + ((((c%25)%10)%5)//1)

print (d, "dollars and", c, "cents are:"  )
print (quarters, "quarters,", dimes, "dimes,", nickels, "nickels,", pennies, "pennies")
