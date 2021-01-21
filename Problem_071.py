#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 17:07:20 2021

@author: edward

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, find the numerator of the fraction immediately to the left of 3/7.

"""
import math
from numba import jit


@jit(nopython=True)
def reduce(n, d):
    # reduces a functions to the smallest common denomiator
    # 6/15 -> 2/5

    g = math.gcd(n, d)

    return int(n / g), int(d / g)


def compare(f1):
    return f1[0] / f1[1]


fractions = set()

for d in range(1, 10):
    if d % 100 == 0:
        print(d)
    # print(d)
    for n in range(1, d):
        # print(n, d)
        nn, dd = reduce(n, d)

        fractions.add((nn, dd))

d = sorted(fractions, key=compare)
