# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 21:58:24 2017

@author: Edward

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.



"""

def next_collatz(n):
    if n % 2 == 0:
        return n/2
    else:
        return n*3 + 1
    
    
long_val = 0
long_length  = 0

for i in range(1,1000000):
    n = i
    sequence = [n]
    while n > 1:
        n = next_collatz(n)
        sequence.append(n)
        
    if len(sequence) > long_length:
        print('new', i,len(sequence))
        long_length = len(sequence)
        long_val = i
        
print(long_val)
        
    
    
    
    
    
    



