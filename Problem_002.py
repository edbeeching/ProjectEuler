# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:40:03 2017

@author: Edward
"""

last1 = 1
last2 = 2
total = 0

while last2 < 4000000:
    if last2 % 2 == 0:    
        total += last2
    last1, last2 = last2, last1 + last2

print(total)