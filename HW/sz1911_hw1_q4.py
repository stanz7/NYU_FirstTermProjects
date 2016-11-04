# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 17:29:18 2016

@author: Stanley Zeng
"""

year = int(input('please enter the amount of years it has been'))
cp = 307357870
"""
31,536,000 seconds in a year
"""
br = 4505143
dr = 2425846
ir = 901029

form = cp + (year * br) - (year * dr) + (year * ir)

print ('The new population is now',form, 'as opposed to', cp)