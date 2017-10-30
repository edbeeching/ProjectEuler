# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 16:41:45 2017

@author: Edward
"""
from myutils import is_prime, rotate
primes = set()
        
        
def is_circular(n):
    for i in range(len(str(n))):
        if int(rotate(str(n),i)) not in primes:
            return False
    return True

for i in range(1,1000000):
    if is_prime(i):
        primes.add(i)
num_circular = 0        
for prime in primes:
    if is_circular(prime):
        num_circular +=1
        
print(num_circular)

