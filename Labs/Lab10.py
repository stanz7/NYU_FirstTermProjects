# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 11:24:23 2016file.

@author: Stanley
"""

def circular_shift_list1(lst,k):
    newlist = lst[-k:] + lst[:-k]
    return(newlist)
    
def average(lst):
    total = 0
    counter = 0
    for i in lst:
        total += i
        counter += 1
    avg = total/counter
    return(avg)
    
def remove_below_avg(lst):
    avg = average(lst)
    elist = []
    for num in lst:
        if (num>avg):
            elist.append(num)
    return(elist)
    
def writeName(filename, firstName, lastName):
    myFile = open(filename, 'w')
    myFile.write(firstName + ' ' + lastName)

def writeRandnumbers(filename, n):
    myFile = open(filename, 'w')
    import random
    while (n > 0):
        num = str(random.randint(0,100))
        myFile.write(num+"\n")
        n-=1
        
def sumColumn(filename):
    myFile = open(filename, "r")
    total = 0   
    for x in myFile:
        total += int(x)
    print(total)
sumColumn("randnum.txt")

    
        