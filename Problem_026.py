# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:10:49 2017

@author: Edward
"""
largest_i = 0
largest_j = 0
for i in range(1,1001):
    frac = 1.0/i
    #print(frac)
    for j in range(2,10000):
        mult = frac * j
        if mult - frac == (mult // 1):
            
            
            if j > largest_j:
                print(i,frac,j,mult - frac)
                largest_j = j
                largest_i = i
            break
        
print(largest_i)