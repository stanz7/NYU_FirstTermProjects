# -*- coding: utf-8 -*-
"""
Created on Sat Nov 26 17:33:19 2016

@author: Stanley
"""

def create_prefix_lists(lst):
    elist =  []
    n = 0
    length = len(lst)
    while(length > 0):
        if n == 0:
            elist.append([])
        else:
            elist.append(lst[:n])
        n += 1
        length -= 1
    elist.append(lst)
    return(elist)
        