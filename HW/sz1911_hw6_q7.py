# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 01:36:50 2016

@author: Stanley
"""
##7

def part7a(phrase):
    for i in range(0, len(phrase)):
        if phrase[i] == " ":
            return phrase[0: i]
            
def part7b(phrase):
    for i in range(0, len(phrase)):
        if phrase[i] == " ":
            return phrase[i + 1: len(phrase)]
            
def part7c(phrase):
    phrasetwo = phrase
    length = len(phrase)
    newstr =""
    liste = []
    for index in range(0, length):
        if phrase[index: index + 1] == " ":
           liste.append(index)
    lengthlist = len(liste)
    while (lengthlist > 0):
        newstr += phrase[liste[lengthlist - 1]:len(phrase)]
        phrase = phrase[0: liste[lengthlist -1]]
        liste = liste[0: (len(liste)-1)]
        lengthlist -=1
    newstr += " " + part7a(phrasetwo)
    newstr = newstr[1:len(newstr)]
    return newstr


def main():
    inp = str(input("Please enter a sentence:"))
    print(part7c(inp))

main()
    