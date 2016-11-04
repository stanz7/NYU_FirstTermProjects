# -*- coding: utf-8 -*-
"""
Created on Fri Oct 28 16:18:22 2016

@author: Stanley
"""


def print_month_calender(num_of_days, starting_day):
    print("Mon","\t","Tue","\t","Wed","\t","Thr","\t","Fri","\t","Sat","\t","Sun")
    print("\t"*(starting_day -1 ), 1,end='')
    num = 2
    while (starting_day < 7):
        starting_day += 1
        if (starting_day == 7):
            print("\t", num, end="\n")
            num += 1
        else:
            print("\t", num,end='')
            num += 1
            
    starting_day = 0
    while (starting_day < 7):
        if (starting_day == 0):
            print(num,end="")
            starting_day += 1
            num+=1
        starting_day += 1
        if (starting_day == 7):
            print("\t", num, end="\n")
            num+=1
        else:
            print("\t", num,end='')
            num += 1
    starting_day = 0
    while (starting_day < 7):
        if (starting_day == 0):
            print(num,end="")
            starting_day += 1
            num+=1
        starting_day += 1
        if (starting_day == 7):
            print("\t", num, end="\n")
            num+=1
        else:
            print("\t", num,end='')
            num += 1
    starting_day = 0
    while (starting_day < 7):
        if (starting_day == 0):
            print(num,end="")
            starting_day += 1
            num+=1
        starting_day += 1
        if (starting_day == 7):
            print("\t", num, end="\n")
            num+=1
        else:
            print("\t", num,end='')
            num += 1
    starting_day = 0
    while (starting_day < 7):
        if (starting_day == 0):
            print(num,end="")
            starting_day += 1
            num+=1
        starting_day += 1
        if (starting_day == 7):
            print("\t", num, end="\n")
            num+=1
        else:
            print("\t", num,end='')
            num += 1
print_month_calender(0,5)