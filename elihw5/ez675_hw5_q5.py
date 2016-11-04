# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 10:44:37 2016

@author: ezhu2
"""

def printed_shifted_triangle(x,y,symbol):
    sym = 1
    space = x
    while sym <= x:
        print(" " * y + " "* space + symbol*(2*sym -1))
        sym += 1
        space -= 1
printed_shifted_triangle(3,4,"+")

def print_pine_tree(n,symbol):
    for i in range(n):
        sym = 1
        space= n
        while sym <= (i ++2) :
            print(" " *space+ symbol *(2*sym-1))
            sym += 1
            space -=1
print_pine_tree(3,"#")

def main():
    input1 = int(input("Input number of triangles:"))
    input2 = str(input("Input your preferred symbol:"))
    print("The tree has",input1,"triangles and has", input2,"as a symbol")
main()