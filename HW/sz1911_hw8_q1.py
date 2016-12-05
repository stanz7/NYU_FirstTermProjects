# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 17:17:52 2016

@author: Stanley
"""

def reverse_to_new_list(lst):
    newlst = []
    n = -1
    length = len(lst)
    while(length > 0):
        newlst.append(lst[n])
        n -= 1
        length -= 1
    return(newlst)

def reverse_in_place(lst):
    length = len(lst)
    for i in range (length//2):
        lst[i], lst[length - 1 - i] = lst[length - 1 - i], lst[i]
    return(lst)

def main():
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse_to_new_list(lst1)
    print("After reverse_to_new_list, lst1 is", lst1, "and the returned list is", rev_lst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    print("Before reverse_in_place, lst2 is", lst2)
    reverse_in_place(lst2)
    print("After reverse_in_place, lst2 is", lst2)