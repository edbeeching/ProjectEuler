# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 15:45:30 2017

@author: Edward

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

import itertools


for i in range(1,10):
    vals = [i for i in range(1,i+1)]
    for permute in itertools.permutations(vals):
        n = sum([a*10**b for b,a in enumerate(permute)])
        if len(set(str(n))) == len(set(str(2*n))) == len(set(str(3*n))) == len(set(str(4*n))) ==len(set(str(5*n))) == len(set(str(6*n))):
            print(n)
        