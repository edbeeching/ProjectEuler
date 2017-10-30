# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:16:55 2017

@author: Edward
"""

summed = 1
total = 3
counter = 1
skipval = 2
while total < 1001*1001:
    print(total)
    summed += total
    counter += 1
    total += skipval
    
    
    if counter > 3:
        counter = 0
        skipval +=2

total
