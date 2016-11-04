# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 11:08:22 2016

@author: Stanley
"""

##Warmup problem 1

language = input("Enter a language:")
if language == "es":
    print ("Hola Mundo")
if language == "en":
    print ("Hello World")
if language == "cn":
    print ("你好，世界")

##Warmup problem 2

num = int(input("Enter a number:"))

if (num%2 == 0):
    print ("Even")
else:
    print ("Odd") 
    
##Problem #1
    
ntc = int(input("Please enter an integer less than 100:"))
ntd = ntc
es = ""


if (50 <= ntc < 100 ):
    es = es + "L"
    ntc = (ntc - 50)
if ( 10 <= ntc < 50):
    es  = es + "X"
    ntc = (ntc -10)
if ( 10 <= ntc < 50):
    es  = es + "X"
    ntc = (ntc -10)
if ( 10 <= ntc < 50):
    es  = es + "X"
    ntc = (ntc -10)
if ( 10 <= ntc < 50):
    es  = es + "X"
    ntc = (ntc -10)    
if (5 <= ntc < 10):
    es = es + "V"
    ntc = (ntc - 5)
if (1 <= ntc < 5):
    es = es + "I"
    ntc = (ntc - 1)
if (1 <= ntc < 5):
    es = es + "I"
    ntc = (ntc - 1)
if (1 <= ntc < 5):
    es = es + "I"
    ntc = (ntc - 1)
if (1 <= ntc < 5):
    es = es + "I"
    ntc = (ntc - 1)
    

print (ntd, "in Roman numerals is:", es)

## Problem #2

name = input("Please enter your name:")
gyear = int(input("Please enter your graduation year:"))
cyear = int(input("Please enter the current year:"))

if (gyear - cyear) > 4:
    print (name, "is not in college yet.")
if (gyear - cyear) == 4:
    print (name, "is a Freshman.")
if (gyear - cyear) == 3:
    print (name, "is a Sophomore.")
if (gyear - cyear) == 2:
 print (name, "is a Junior.")
if (gyear - cyear) == 1:
 print (name, "is a Senior.")
if (gyear - cyear) <= 0:
 print (name, "is Graduated.")
 
## Problem #3

hr = int(input("Please enter time in 24 hr format:"))
hour = (hr//100)
min = (hr%100)

if hour <= 12:
    print(str(hour) + ":" + str(min) + "am")
if hour > 12:
    hour = hour - 12
    print (str(hour) + ":" + str(min) + "pm")

## Problem #4

a = float(input("Please enter the first leg:"))
b = float(input("Please enter the second leg:"))
c = float(input("Please enter the hypotenuse:"))

if (((a*a) + (b*b)) == (c*c)):
    print (a, ",", b, "and", str(c), "form a right triangle.")
else:
    print (a, ",", b, "and", str(c), "do not form a right triangle.")
    
## Problem #5


a = float(input("Please enter a:"))
b = float(input("Please enter b:"))
zero = 0
if (a == 0) and (b != 0):
    print ("NO SOLUTION")
if (a == 0) and (b == 0):
    print ("Infinite solutions")
else:
    val = (zero -b)/a
    print ("x = ", val)

     
    
    
    

    
    