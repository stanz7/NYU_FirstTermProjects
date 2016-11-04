# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 21:49:46 2016

@author: Stanley
"""

print("Please enter a sentence in English. ")
print("Separate the words with a single space.")
sentence = input("Enter your sentence here: ")
space_count = 0
for letter in sentence:
    if (letter == " "):
        space_count +=1
print("There are", space_count + 1, "words")