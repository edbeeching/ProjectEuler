#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 20:30:50 2018

@author: edward


It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?


"""
import matplotlib.pyplot as plt
import numpy as np

def frac_add(v, n, d):
    vd = v*d
    
    return vd+n, d

def frac_div(v,n,d):
    return frac_mult(v,d,n)
    
def frac_mult(v,n,d):
    return v*n, d    

def get_frac(x):
    
    n,d = 1,2
    
    for i in range(x-1):
        n,d = frac_add(2, n, d)
        n,d = frac_div(1, n, d)
            
        
    return frac_add(1, n, d)
    
    
    
    return n,d 

def is_greater(n,d):
    
    return len(str(n)) > len(str(d))

results = 0

for i in range(1,1001):
    n,d = get_frac(i)
    
    if is_greater(n,d):
        print(i, n, d)
        results += 1
    
print(results)
