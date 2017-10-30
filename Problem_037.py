# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:41:39 2017

@author: Edward
"""

from myutils import is_prime


def is_truncatable(n):
    if n < 10:
        return False
    for i in range(1,len(str(n))):
        if int(str(n)[i:]) not in primes:
            return False
        if int(str(n)[:i]) not in primes:
            return False
    return True
        



primes = set([2])
sum_truncs = 0
num_truncs = 0

val = 3
while num_truncs < 11:
    if is_prime(val):
        primes.add(val)
        
        if is_truncatable(val):
            
            num_truncs += 1
            sum_truncs += val
            print('new trunc', val, num_truncs)
    val += 2
    
print(sum_truncs)

    
    