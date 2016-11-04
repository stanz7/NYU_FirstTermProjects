# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 22:06:23 2016

@author: ezhu2
"""

def print_month_calender(num_of_days, starting_day):
    print("Mon","\t","Tue","\t","Wed","\t","Thr","\t","Fri","\t","Sat","\t","Sun")
    print("\t"*(starting_day -1 ), 1)
print_month_calender(31,4)