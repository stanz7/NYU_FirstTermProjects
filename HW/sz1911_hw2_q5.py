# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 01:17:40 2016

@author: Stanley
"""

"""
#5
"""

jdays = int(input("Please enter the number of days John has worked:"))
jhours = int(input("Please enter the number of hours John has worked:"))
jmins = int(input("Please enter the number of minutes John has worked:"))
bdays = int(input("Please enter the number of days Bill has worked:"))
bhours = int(input("Please enter the number of hours Bill has worked:"))
bmins = int(input("Please enter the number of minutes Bill has worked:"))
days = (jdays + bdays)
hours = (jhours + bhours)
if (hours) >= 24:
    days = days + 1
    hours = hours - 24
else:
    days + 0
    
mins = (bmins + jmins)

if(mins) >= 60:
    hours = hours + 1
    mins = mins - 60
else:
    hours + 0
    

print ("They have worked", days, "days", hours, "hours and", mins, "mins")