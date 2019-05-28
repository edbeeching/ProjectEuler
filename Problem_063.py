#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 19:56:26 2018

@author: edward


The 5-digit number, 16807=7**5, is also a fifth power. Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""




total = 0
powers = set()
for i in range(1,10):
    print('#'*10)
    power = 1
    while True:
        n = i**power
        
        if len(str(n)) == power:
            print(i, n, power)
            total += 1
            powers.add(n)
            
        if len(str(n)) < power:
            print('break')
            break
        power += 1



print(len(powers))


