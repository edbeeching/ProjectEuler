# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:45:30 2017

@author: Edward

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

import itertools


    
def check(n):    
    v = sorted(str(n))    
    for i in range(2,7):
        nn = n*i
        if sorted(str(nn)) != v:
            return False
    return True
    
    

for n in range(1, 1000000):
    if check(n):
        print(n, 2*n, 3*n, 4*n, 5*n, 6*n)
    