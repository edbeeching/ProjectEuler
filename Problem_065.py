#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 14:34:21 2019

@author: edward

Convergents of e

"""


def calc_frac(l, n, d):
    # return n/d . eg is l = 2 n = 3 and d = 5 this return (l*d + n) / d  = 13 / 5
    
    return (l*d + n) , d

def flip_frac(n, d):
    
    return d, n
    
    
    

def calculate_fraction(array):
    
    if len(array) == 2:
        l = array[0]
        n = 1
        d = array[1]
        return calc_frac(l,n,d)
    else:
        l = array[0]
        n,d =  flip_frac(*calculate_fraction(array[1:]))
        
        return calc_frac(l, n, d)
        
   


     
e = [2]

for k in range(1,1000):
    e += [1, 2*k, 1]

print(1, 2)
for i in range(2,101):
    n, d = calculate_fraction(e[:i])
    #print(i,n)
    print(i, sum([int(v) for v in str(n)]))


    
