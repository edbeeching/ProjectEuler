# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:11:44 2017

@author: Edward
"""

from myutils import get_divisors

def lowest_common(numer, denom):

    numer_divisors = get_divisors(numer)[1:]
    denom_divisors = get_divisors(denom)[1:]
    common_divisors = [n for n in set(numer_divisors) if n in set(denom_divisors)]
    
    if len(common_divisors) > 0:
        max_common_divisor = common_divisors[-1]
        return int(numer/max_common_divisor), int(denom/max_common_divisor)
    return numer, denom
    
    
    
    
for i in range(10,100):
    for j in range(i+1,100):
        if (i,j) != lowest_common(i,j) and (i%10 !=i//10) and (j%10!=j//10):
            
            if (int(str(i)[0]), int(str(j)[1])) == lowest_common(i,j):
                print(i,j)