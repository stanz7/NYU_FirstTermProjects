# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 11:33:27 2016

@author: Stanley
"""
##1
x = int(input("Please enter a positive integer:"))
n = int(input("Please enter the number of digits:"))
sum = 0
while n > 0:
    sum += (x%10)
    x = x // 10
    n -= 1
print (sum)


##2

positive = int(input("Please enter a positive integer:"))
sumt = 0

while (positive > 0):
    if positive % 2 == 1:
        sumt += positive
    if positive % 2 == 0:
        sumt -= positive
    positive -= 1

print (sumt)


##3
dividend = int(input("Please enter a positive integer as the dividend:"))
divisor = int(input("Please enter a positive integer as the divisor:"))
count = 0
while (dividend > divisor):
    count += 1
    dividend -= divisor
print (count)

##4
a = int(input("Please enter a positive integer as a dividend:"))
b = int(input("Please enter a positive integer as a divisor:"))
while (a >= b):
    a -= b
print (a)

##5
y = int(input("Please input a positive integer:"))
n = 1
z = n
p = n

while (y > 0):
    lll = (z*z*z)
    print (lll)
    z += 1
    y -= 1

while ((p**2) < y):
    ll = (p*p*p)
    print(ll)
    p += 1
if (1 <=  y <= 5):
    print (y**3)

##6
num = int(input("Please input a positive integer:"))
w = num
while w >=1:
    print((num -w)*"x" + "o" + str((w-1)* "x") + "\n")
    w -= 1
    
            
