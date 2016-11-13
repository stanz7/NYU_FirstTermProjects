# -*- coding: utf-8 -*-
"""
Created on Fri Nov 11 11:40:54 2016

@author: Stanley
"""
##1a

def count(lst, item):
    counter = 0
    for i in lst:
        if(i == item):
            counter += 1
    print(counter)
    
##1b
    
def power(n):
    lst = []
    counter = 1
    while (n > 0):
        lst.append(2**counter)
        n -= 1
        counter += 1
    print(lst)
    
##1c

def find_max_even_index(lst):
    location = 0
    max_even = 0
    counter = -1
    for i in lst:
        counter += 1
        if (i % 2 == 0) and (i > max_even):
            max_even = i
            location = counter
    print(location)
    return location

##1d

def circular_shift_list1(lst, k):
    newlist = lst[-3:]+lst[:-3]
    return(newlist)

##2

def get_Common_Ele(list1, list2):
    ce = []
    for items in list1:
        if items in list2 and items not in ce:
            ce.append(items)
    return(ce)

##3a
def list_square_sum(lst):
    sum = 0
    for i in lst:
        sum += (i**2)
    return(sum)

##3b
def main3b():
    myList = []
    flag = True
    while flag:
        newItem = input("Enter Item:")
        if newItem != "done":
            myList.append(int(newItem))
        else:
            flag = False
    print(list_square_sum(myList))

##4

import random
def generateBoard():
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    symbols =['X','O','-']
    for i in range(3):
        for j in range(3):
            board[i][j] = symbols[random.randint(0,2)]
    return board

def checkboard(board):
    for i in range(3):
        if board[0][i] != "-" and board[0][i] == board[1][i] and board [1][i] == board [2][i]:
            print(board[0][i],"Won")
            break
        break
    for i in range(3):
        if board[i][0] != "-" and board[i][0] == board[i][1] and board [i][1] == board[i][2]:
            print(board[i][0] ,"Won")
            break
        break
    for i in range(3):
        if board [0][2]!= "-" and board[0][2] == board[1][1] and board [1][1] == board[2][0]:
            print(board[0][2],"Won")
            break
        break
    for i in range(3):
        if board [0][0]!= '-' and board[0][0] == board[1][1] and board [1][1] == board[2][2]:
            print(board[0][0],"Won")
            break
        break
##main function
def main():
    count([0, 32, "a", "0", "4", 15, "q", "0"], "0") 
    power(4)
    find_max_even_index([0,2,10,23,59,48,86,97,99])
    return circular_shift_list1([1,2,3,4,5,6,7,8], 3)

def main2():
    board = generateBoard()
    result  = checkboard(board)
    print(result)
    return get_Common_Ele( [ 2, 'S', 3.13, 3.13, "Python" ], [ "Pythy", 2, 12, "hello", 3.13 ])
    