# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:22:57 2017

@author: Edward
"""
import math

def find_val():
    for a in range(500):
        for b in range(500):
            c = math.sqrt(a*a + b*b)
            if c == round(c) and (a+b+c) == 1000:
                print(a*b*c)
                return
            
        
find_val()
    