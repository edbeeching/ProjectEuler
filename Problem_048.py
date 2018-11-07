# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 20:41:05 2017

@author: Edward
"""

tot = 0
for i in range(1,1001):
    tot += i**i
    
print(str(tot)[-10:])