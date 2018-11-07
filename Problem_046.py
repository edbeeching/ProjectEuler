# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 11:36:35 2017

@author: Edward

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×12
15 = 7 + 2×22
21 = 3 + 2×32
25 = 7 + 2×32
27 = 19 + 2×22
33 = 31 + 2×12

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

"""

from myutils import is_prime

import math
    
def is_goldbach(n):
    for p in primes:
        if p > n+2: 
            break
        residual = math.sqrt((n-p)//2)
        if residual // 1 == residual:
            return True
    
    
    return False
    
    
primes = set([2])    
    
for i in range(3,100000,2):
    if is_prime(i):
        primes.add(i)
    else:
        if not is_goldbach(i):
            print(i)
            break
        
        
    
    
    
        