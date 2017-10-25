# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:09:10 2017

@author: Edward
"""
import math
def get_divisors(num):
    divs = set()
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            divs.add(i)
            divs.add(num//i)
    return sorted(list(divs))

tri = 0
i = 1
num_divs=0
while num_divs <= 500:
    tri += i
    i += 1
    num_divs = len(get_divisors(tri))

print(tri)   