#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 22:24:55 2018

@author: edward

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

"""


def digital_sum(n):
    n = str(n)
    return sum([int(v) for v in n])


largest = 0

for a in range(100):
    for b in range(100):
        n = a**b
        c = digital_sum(n)
        largest = max(c, largest)
        
        
print(largest)
            
            
        