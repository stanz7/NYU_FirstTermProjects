# -*- coding: utf-8 -*-
"""
Created on Thu Oct  6 23:58:17 2016

@author: Stanley
"""

itema = float(input("Please enter the price of item 1:"))
itemb = float(input("Please enter the price of item 2:"))
cc = (input("Please enter Y if you have a card, N if not:"))
tax = float(input("Please enter the tax rate:"))
baseprice = (itema + itemb)
newprice = 0

print (baseprice)
if (cc == "Y"):
    if (itema > itemb):
        newprice = (newprice + itema + (itemb * .5))*.9
        print (newprice)
        print (newprice + (newprice * (tax/100)))
    if (itemb > itema):
        newprice = (newprice + itemb + (itema * .5))*.9
        print (newprice)
        print (newprice + (newprice * (tax/100)))
if (cc == "N"):
    if (itema > itemb):
        newprice = (newprice + itema + (itemb * .5))
        print (newprice)
        print (newprice + (newprice * (tax/100)))
    if (itemb > itema):
        newprice = (newprice + itemb + (itema * .5))
        print (newprice)
        print (newprice + (newprice * (tax/100)))