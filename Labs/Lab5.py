# -*- coding: utf-8 -*-
"""
Created on Fri Oct 14 12:02:51 2016

@author: Stanley
"""

##1

pos_int = int(input("Input a positive integer:"))
num = 1
if (pos_int == 0):
    print (0)
while (pos_int > 0):
    num = (num* pos_int)
    pos_int -= 1
print (num)

##2

dage = int(input ("Please enter how old your dog is in human years:"))
hage = 0
dagem = (dage - 2)
hagem = 21

if (dage <= 2):
    hage += (10.5 * dage)
    print (hage)
while (dage > 2):
    hagem += 4
    dage -= 1
print (hagem)

##3

a = int(input ("input integer a:"))
b = int(input ("input integer b:"))
counter = 0

while (a>0):
    if (a%10 != b%10):
        counter += 1
    a = a//10
    b = b//10
print (counter)
