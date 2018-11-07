# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:37:40 2017

@author: Edward

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.

"""
import math

tot = 0
for i in range(3,1000000):
    
    t = 0
    
    for v in str(i):
        t += math.factorial(int(v))
    
    if t == i:
        tot+=i
        print(i)


print(tot)