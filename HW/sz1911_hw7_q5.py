# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:47:53 2016

@author: Stanley
"""

def find_all(lst, val):
    elist = []
    hold = 0
    for i in lst:
        if i == val:
            elist.append(hold)
        hold += 1
    return (elist)
            