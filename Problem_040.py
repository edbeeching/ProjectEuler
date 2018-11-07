#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 21:47:01 2018

@author: edward

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000


"""
import matplotlib.pyplot as plt
import numpy as np


ds = [10**i for i in range(6)]
v=[]
i = 0
while len(v) < 1000000:
    i += 1
    str_i = str(i)
    v += [int(j) for j in str_i]
    

result = 1

for d in ds:
    result*=v[d-1]

print(result)
