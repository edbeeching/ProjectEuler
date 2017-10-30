# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:13:48 2017

@author: Edward
"""
def triagonal(n):
    return int(n*(n+1)/2)

def pentagonal(n):
    return int(n*(3*n-1)/2)

def hexagonal(n):
    return int(n*(2*n-1))


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

def is_composite(n):
    return not is_prime(n)


def get_divisors(num):
    divs = set()
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            divs.add(i)
            divs.add(num//i)
    return sorted(list(divs))

def is_pandigital(n, digits=9):
    if len(str(n)) != 9:
        return False
    
    if len(set(str(n))) == len(str(n)):
        return True
    return False
    
    
    
    
    
    
    
    
    
    


def rotate(s,r):
    return s[r:] + s[:r]