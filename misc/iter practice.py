# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 16:54:01 2016

@author: Stanley
"""

str = "stanley"

for x in str:
    print (x),
print
    
it = iter(str)

for x in str:
    if ((it.__next__()) == "l"):
        break
    print (it.__next__())

    
"""
print (it.__next__())
print (it.__next__())
print (it.__next__())

print (list(it))
"""
