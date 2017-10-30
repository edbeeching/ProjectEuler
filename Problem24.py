# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:30:29 2017

@author: Edward
"""

import math

math.factorial(9)

digits = set([0,1,2,3,4,5,6,7,8,9])

total = 1000000

digits_out = []
for i in [9,8,7,6,5,4,3,2,1,0]:
    count = 0    
    val_ind = 0
    while(count < total):
        count += math.factorial(i)
        val_ind += 1
        
    count -= math.factorial(i)
    total -= count
    digits_out.append(list(digits)[val_ind-1])
    digits.remove(list(digits)[val_ind-1])
    if total == 0:
        digits_out += list(digits)
        
print(digits_out)