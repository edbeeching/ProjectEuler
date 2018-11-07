# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:12:25 2017

@author: Edward

A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def check_palidromic(val):
    if str(val) == str(val)[::-1]:
        return True
    else:
        return False

largest = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        product = i*j
        if product > largest and check_palidromic(product):
            largest = product
            
print(largest)
            