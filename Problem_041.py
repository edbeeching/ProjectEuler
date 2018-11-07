# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 15:36:05 2017

@author: Edward


We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

"""

import itertools
from myutils import is_prime

largest = 0

for i in range(2,11): 
    vals = [i for i in range(1,i)]
    for permute in itertools.permutations(vals):
        val = sum([a*10**b for b,a in enumerate(permute[::-1])])
        if is_prime(val):
            if val > largest:
                largest = val
    
    
print(largest) 