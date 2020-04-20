#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 16:55:17 2018

@author: edward

The cube, 41063625 (345**3), can be permuted to produce two other cubes: 56623104 (384**3) and 66430125 (405**3). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""
    
perm_keys = {}

n=1
found = False
while not found:
    cube = n**3
    key = tuple(sorted(str(cube)))
    if key in perm_keys.keys():
        perm_keys[key].append(cube)
        if len(perm_keys[key]) == 5:
            print(perm_keys[key])
            print(min(perm_keys[key]))
            found = True
    else:
        perm_keys[key] = [cube]
    
    n +=1
    
    














