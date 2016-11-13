# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 11:19:13 2016

@author: Stanley
"""
"""
##1
string = input("Please enter a string of 1s and 0s:")
retstr = " Your String has \n:"
currentpos = 0  
while (currentpos < len(string)):
    counter = 1
    flag = string[currentpos]
    currentpos += 1
    while(currentpos < len(string) and flag == string[currentpos]):
        counter += 1
        currentpos += 1
    retstr += str(counter) + " " + flag + "s\n"
    
print(retstr)

##2a

def part2a(ch, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    retstr = ""
    counter = 0
    index = alphabet.index(ch)
    while (n > 0):
        if (index + counter == 26):
            index = 0
            counter = 0
        retstr += alphabet[index + counter]
        counter += 1
        n -= 1
    print(retstr)


##2b

def part2b(myint, n):
    lista = []
    while (n > 0):  
        lista.append(myint)
        myint += 1
        n -= 1
    print(lista)
"""
"""
##3a
x                    v

    
##3b
def multifind(some_string, substring, start, end):
    n = len(substring)
    liste = []
    last = end - n #last positive position that we can find the substr
    for left_ind in range(start, last+1): #left_index keeps track of where the substr might be starting in some_string
        if some_string[left_ind: left_ind+n] == substring: #starting from left_ind till leftend + length of substring
            liste.append(left_ind)
    if not liste:
        print ("Couldn't find it")
    else:
        print(liste)
        
##3c
def main():
    stra = "ATCGTACGTATACG"
    strb = "ACGTACAATGCATA"
    strc = "AACTGACGATA"
    strd = "ATCGATCGATCG"
    multifind(stra, "CG", 0, len(stra))
    find(stra, "CG", 0, len(stra))
    multifind(strb, "A", 0, len(strb))
    find(strb, "TA", 0, len(strb))
    multifind(strc, "B", 0, len(strc))
    multifind(strd, "ATCG", 0, len(strd))
    
main()
"""
    