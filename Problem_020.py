# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 23:25:28 2017

@author: Edward

n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!


"""


total = 1

for i in range(1,101):
    total*=i

print(sum([int(j) for j in str(total)]))