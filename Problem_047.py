#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 16:34:55 2019

@author: edward

Distinct prime factors

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?


"""

from myutils import get_prime_factors


def get_factors(n):
    # eg for 644 returns [(2,2), (7,1), (23,1)]
    found = set()
    factors = []
    prime_factors = get_prime_factors(n)
    
    for factor in prime_factors:
        if factor in found:
            continue
        found.add(factor)
        num = prime_factors.count(factor)
        factors.append((factor, num))

    return tuple(factors)
    
    

NUM_CONS = 4
    
    
for i in range(2,10000000):
    
    combined_factors = set()
    distinct = True
    if len(get_factors(i)) != NUM_CONS:
        distinct = False 
        continue
    for j in range(i,i+NUM_CONS):
        factors = get_factors(j)
        if len(factors) != NUM_CONS:
            distinct = False
            break
        #print(j, factors)
        for factor in factors:
            if factor in combined_factors:
                distinct = False
            else:
                combined_factors.add(factor)
            
    if distinct:
        print(i, combined_factors)
        break
        
            

