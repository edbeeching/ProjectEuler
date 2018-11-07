# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 16:54:59 2017

@author: Edward


Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""
names = []
with open('p022_names.txt') as f:
    names = f.readlines()[0].split(',')
    
names = sorted(names)    
letter_scores = {}
for i, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
    letter_scores[letter] = i+1
letter_scores['"'] = 0


total = 0
for i, name in enumerate(names):
    total+= (i+1)*sum([letter_scores[n] for n in name])
    
print(total)