# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:45:02 2017

@author: Edward

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?

"""

import itertools
def is_concatenated_product(n, v=2, base=None):
    n_string = str(n)
    for i in range(1,len(n_string)):
        start = n_string[:i]
        end = n_string[i:]
        if base == None:
            double = str(int(start)*v)
            b = start
        else:
            double = str(int(base)*v)
            b=base
        
        if double == end:
            return True        
        if end.find(double) == 0:
            if is_concatenated_product(end,v+1,b):
                return True  
    return False


print(is_concatenated_product(192384576))

largest = 0

for i in range(2,11): 
    vals = [i for i in range(1,i)]
    for permute in itertools.permutations(vals):
        val = sum([a*10**b for b,a in enumerate(permute[::-1])])
        
        if is_concatenated_product(val):
            print(val)


