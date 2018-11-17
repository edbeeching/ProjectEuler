#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 19:31:53 2018

@author: edward
"""


from myutils import is_prime

def triangle_generator():
    
    yield [1]
    ind = 1 
    next_size = 3
    
    while True:
        num_vals = (next_size-2)*4 + 4
        values = list(range(ind+next_size-1, num_vals+ind+1, next_size-1))
        
        ind = values[-1]
        
        next_size += 2
        yield values
    

num_primes = 0
total = 1

for size, vals in zip(range(1,100001,2), triangle_generator()):
    if vals == [1]:
        continue
    
    total += len(vals)
    
    for v in vals:
        if is_prime(v):
            num_primes +=1
    
    if num_primes / total < 0.1:
        print(size)
        break

    
    
