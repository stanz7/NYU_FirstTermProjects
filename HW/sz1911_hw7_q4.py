# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 23:30:11 2016

@author: Stanley
"""

def max_abs_val(lst):
    compare = abs(lst[0])
    for i in lst:
        val = abs(i)
        if (compare < val):
            compare = val
    print(compare)
    
