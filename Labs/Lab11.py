# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 11:26:12 2016

@author: Stanley
"""
##2a
def read_menu(filename):
    myDict = {}
    myFile = open(filename, "r")
    for i in myFile:
        myString = i
        mySplit = myString.split(": $")
        item = mySplit[0]
        price = mySplit[1]
        s = price[: len(price) - 1]
        myDict[item] = float(s)
    return(myDict)
    

##2b

def read_customer_order():
    list = []
    flag = True
    print("What would you like to order?")
    while flag:
        order = input("")
        if order == "done":
            flag = False
        else:
            list.append(order)
    return(list)

##2c

def compute_price(menu_dictionary, order_list):
    myFile = read_menu(menu_dictionary)
    price = 0
    for i in order_list:
        price += myFile.get(i)
    return(price)
    
##2d

def main():
    n = 3
    while ( n > 0):
        menu = input("Please enter a file name that contains a menu:")
        mylist = read_customer_order()
        price = (1.085 * compute_price(menu, mylist))
        return(round(price, 2))
        n -= 1
        
##3

def check(phonenumber):
    if len(phonenumber) != 10 or phonenumber.isdigit == False:
        return False
    else:
        return True



def add_entry(phonebook, name, phonenumber):
    legit = check(phonenumber)
    if (legit == True) and (name not in phonebook):
        phonebook[name] = phonenumber
    else:
        print("Sorry, this isn't a valid phone number, or this name is already in the phonebook")

def lookup(phonebook, name):
    if name in phonebook:
        return phonebook.get(name)
    else:
        print("Sorry, that name doesn't exist")

def print_all(phonebook):
    for i in phonebook:
        print(i)

def mainthree():
    myDict = {}
    myFile = open("phonebookk.txt", "r")
    for i in myFile:
        n = i.split(" ")
        name = n[0] + n[1]
        number = n[2]
        add_entry(myDict, name, number[:len(number) -1])
    print_all(myDict)
    return(myDict)

    


        

