# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:10:23 2017

@author: Edward

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""



result = sum([int(x) for x in str(2**1000)])
print(result)