# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:02:34 2017

@author: Edward
"""


last1 = 1
last2 = 1
total = 0

index = 2
while True:
    if last2 % 2 == 0:    
        total += last2
    last1, last2 = last2, last1 + last2
    index += 1 
    if len(str(last2)) == 1000:
        break
    
    
    

print(index, last2)