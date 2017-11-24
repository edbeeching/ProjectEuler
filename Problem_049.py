# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 21:05:29 2017

@author: Edward

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""
from myutils import is_prime
primes = set()
for i in range(1001, 10000, 2):
    if is_prime(i):
        primes.add(i)    
    

for prime in primes:
    for i in range(1, 10000-prime):
        
        
        if prime + i in primes and prime + 2*i in primes and sorted(str(prime + i)) == sorted(str(prime)) and sorted(str(prime + 2*i)) == sorted(str(prime)):
            print(prime, prime + i, prime + 2*i,  i)
    