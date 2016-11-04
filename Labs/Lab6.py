# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 11:38:38 2016

@author: Stanley
"""
##1a

n = int(input("enter integer n:"))
holder = n
c = 1
ct = 0

while (n > 0):
    print (" " * holder + "*" * (c + ct))
    c += 1
    ct += 1
    n -= 1   
    holder -=1
    

##1b

num = int(input("enter integer n:"))
hold = num - 1
counter = 0


while (num > 0):
    print ("#" * counter + "%" + "$" * hold)
    hold -= 1
    counter +=1
    num -=1
"""
##1bforloop
n = int(input("enter n:"))
i = 0
for i in range(i,n+1):
    for j in range(i,n+1):
        if i > j:
            print("$", end= "")
        elif i < j:
            print("#", end= "")
        else:
            print("%", end= "")
        print ("")

n = int(input("enter n:"))
for i in range (i,n+1):
    for j in range(i)

"""
##2
   

def numtwo(n):
    holder = n - 1
    numtodisp = 1
    while ( n > 0):
        print ("." * holder + str(numtodisp) * numtodisp)
        numtodisp += 1
        holder -= 1
        n-=1

##3

from random import randint

theRandomNum = randint(0,101)
print ("I thought of a number between 1 through 100! Try to guess it!")
inp = int(input("Your guess:"))
while (inp != theRandomNum):
    if (inp > theRandomNum):
        print ("My number is smaller than yours")
    if (inp < theRandomNum):
        print ("My number is greater than yours")
    inp = int(input("Your Guess:"))
if (inp == theRandomNum):
    print ("You got it!")
