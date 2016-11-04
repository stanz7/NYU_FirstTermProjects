# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 00:35:21 2016

@author: Stanley
"""

day = input("Enter the day the call started at:")
time = int(input("Enter the time the call started at(hhmm):"))
duration = int(input("Enter the duration of the call(in minutes):"))
bill = 0
weekday = ("Mon", "Tues", "Wed", "Thurs", "Fri")
weekend = ("Sat", "Sun")

if day in weekday:
    if (800 <= time <= 1800):
        bill = bill + (1 * (duration * .40))
        print ("This call will cost:", bill)
    if (time < 800 | time > 1800):
        bill = bill + (1* (duration * .25))
        print ("This call will cost:", bill)

if day in weekend:
    if (800 <= time <= 1800):
        bill = bill + (1 * (duration * .15))
        print ("This call will cost:", bill)
    if (time < 800 | time > 1800):
        bill = bill + (1* (duration * .15))
        print ("This call will cost:", bill)

