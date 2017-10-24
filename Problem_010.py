# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 19:33:21 2017

@author: Edward
"""
import math

def is_prime(number):
    # Code taken for wikipedias entry on prime numbers, but fairly simple
    if number <= 1:
        return False
    elif number <=3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i=5
    while i*i <= number:
        if number % i == 0 or number % (i+2) == 0:
            return False
        i += 6
    return True


prime_sum = 2
for i in range(1, 2000000, 2):
    if is_prime(i):
        prime_sum += i
        
print(prime_sum)
