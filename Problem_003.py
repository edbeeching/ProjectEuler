# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:44:11 2017

@author: Edward
"""

def find_largest_prime(number):
    for i in range(3, number, 2):
        if number % i == 0:
            return find_largest_prime(number//i)
    return number

print(find_largest_prime(600851475143))
