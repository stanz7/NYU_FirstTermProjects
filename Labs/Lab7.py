# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 11:22:23 2016

@author: Stanley
"""

##1

s = input("Input a string s:")

Up = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z, "
Low = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z, "
string = ""

for i in range(len(s)):
    if (s[i] in Low):
        num = Low.index(s[i])
        string += (Up[num])
    if (s[i] in Up):
        num = Up.index(s[i])
        string += (Low[num])
    
print(string)
    
        
##2

s1 = input("Input name1:")
s2 = input("Input name2:")

s1 = s1.split(", ")
s2 = s2.split(" ")
if(s2[1] == s1[0] and s2[0]==s1[1]):
    print("The Two names are equal!")
else:
    print("The two names are not equal")
    




##3a

s = input("Input a string:")
char = input("Input a char:")
num = 0

for i in range(len(s)):
    if (s[i] == char):
        num += 1
print(char, "appears", num, "times in the string.")

##3b

st = input("Input a string:")
chart = input("Input a char:")
length = len(st)
numt = 0
hold = 0
while (length>0):
    if (st[hold] == chart):
        numt +=1
    hold +=1
    length -= 1
    
    
print(chart, "appears", numt, "times in the string.")\


##4
integer = input("Please enter a string representation of an integer:")
even = 0
odd = 0

for i in range(len(integer)):
    if ((int(integer[i]))%2 == 0):
        even += 1
    else:
        odd += 1
           
print("There are", even, "even integer(s)", "and", odd, "odd integer(s)")

integer = input("Please enter a string representation of an integer:")
integ = int(integer)
even = 0
odd = 0

while (integ>0):
    if(integ%2==0):
        even += 1
        integ = integ//10
    else:
        odd +=1
        integ = integ//10

print ("There are", even, "evens", "and", odd, "odds")     
"""   