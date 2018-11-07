# -*- coding: utf-8 -*-
"""
Created on Tue Oct 31 08:44:56 2017

@author: Edward

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""

from myutils import is_prime
primes = set([2])

for i in range(3, 1000000,2):
    if is_prime(i):
        primes.add(i)
        
primes_list = sorted(list(primes))  
print(len(primes_list))  

  

most_con = 1
start_prime = 0

for i in range(78498):  
    
    if i + most_con >= 78498: break
    total = sum(primes_list[i:i + most_con])
    print(i, total, total in primes)
    if total > 1000000: break
    
    for j, prime in enumerate(primes_list[i + most_con:],most_con+1):  
        total += prime
        if total > 1000000: break
        if total in primes:
            if (j-i) > most_con:
                most_con = j-i
                print(i, most_con, total)
                start_prime = i
                
print(most_con, start_prime)
        

        
        
        
    