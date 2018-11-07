# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 19:05:18 2017

@author: Edward
"""

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


def quad_prime(a,b,n):
    return n*n + a*n + b
    

def check_primes(a,b):
    index = 1
    while True:
        potential_prime = quad_prime(a,b,index)
        if is_prime(potential_prime):
            index+= 1
        else:
            break
        
    return index-1

best_a_b = None
best_conseq = 0

for a in range(-999,1000):
    for b in range(-1000,1001):
        conseqs = check_primes(a,b)
        if conseqs > best_conseq:
            best_conseq = conseqs
            best_a_b = (a,b)
        
print(best_conseq, best_a_b)
        
    
    