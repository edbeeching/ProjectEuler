#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 21:54:16 2018

@author: edward


The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes 
and concatenating them in any order the result will always be prime.
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.


"""


from myutils import is_prime

import itertools
# set of primes
# 

primes = set()

def memo_is_prime(n):
    if n in primes:
        return True
    
    if is_prime(n):
        primes.add(n)
        return True
    
    return False
    
    
def is_pair(p1, p2):
    if p1 == p2:
        return False
    n = int(str(p1) + str(p2))
    n2 = int(str(p2) + str(p1))
    
    return memo_is_prime(n) and memo_is_prime(n2)
        
    
def is_nlet(list_of_primes):
    if len(list_of_primes) != len(set(list_of_primes)):
        #print('cant have two of the same in list')
        return False
    
    for i, p1 in enumerate(list_of_primes[:-1],1):
        for p2 in list_of_primes[i:]:
            #if p1 == p2: continue
            if not is_pair(p1, p2):
                return False
            
    return True 
        
        
pairs = set()
triplets = set()
quads = set()
quins = set()
primes.add(2)
n = 3

found = False

prime_list = [2]


while n < 2000:
    if memo_is_prime(n):
        prime_list.append(n)
        
for prim        



while not found:
    if memo_is_prime(n):
        prime_list.append(n)
        print(n, len(primes), len(prime_list), len(pairs), len(triplets), len(quads))
        for p in prime_list:
            if is_pair(n,p):
                cand = tuple(sorted((n,p)))
                pairs.add(cand)
                
                for pair in pairs:
                    if found: break
                    cand = tuple(sorted((*pair, n)))
                    if is_nlet(cand):
                        triplets.add(cand)
                        
                        for trip in triplets:
                            if found: break
                            cand = tuple(sorted((*trip, n)))
                            if is_nlet(cand):
                                quads.add(cand)
                                for quad in quads:
                                    if found: break
                                    cand = tuple(sorted((*quad, n)))
                                    if is_nlet(cand):
                                        quins.add(cand)
                                        print(cand)
                                        found=True
    n += 2



# while n < 2000:
#     memo_is_prime(n)
#     n = n+2
# print('Primes generated')
# prime_list = list(primes)
# for i, p1 in enumerate(prime_list[:-1], 1):
#     print(i)
#     for p2 in prime_list[i:]:
        
        
        
#         if (p1,p2) not in pairs and is_pair(p1,p2):
#             s = tuple(sorted((p1,p2)))
#             pairs.add(s)

# for i, pair in enumerate(list(pairs)[:-1], 1):
#     print(i)
#     for pair2 in list(pairs)[i:]:
#         p1,p2 = pair
#         p3,p4 = pair2
        
#         vals = set([p1,p2,p3,p4])
        
#         for comb in itertools.combinations(list(vals),3):
#             if tuple(sorted(comb)) not in triplets and is_nlet(comb):
#                 s= tuple(sorted(comb))
#                 triplets.add(s)
        
