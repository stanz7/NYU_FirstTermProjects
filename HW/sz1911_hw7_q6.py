# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:52:04 2016

@author: Stanley
"""

def add_list(lst1, lst2):
    elist = []
    hold = 0
    if len(lst1) == len(lst2):
        for i in lst1:
            elist.append(i+lst2[hold])
            hold += 1
        return(elist)
    else:
        return("Lists aren't equal")
    
    

def main():
    list1 = []
    list2 = []
    flag = True
    flag2 = True
    while flag:
        inp = input("Please enter numbers, and type done when you're done:")
        if inp != "done":
            list1.append(int(inp))
        else:
            flag = False
    while flag2:
        inp2 = input("Please enter the second list of numbers, type done when you're done:")
        if inp2 != "done":
            list2.append(int(inp2))
        else:
            flag2 = False
    print(add_list(list1,list2))
            