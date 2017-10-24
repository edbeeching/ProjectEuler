# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:57:27 2017

@author: Edward
"""

def is_prime(number):
    for i in range(3,number,2):
        if number %i == 0:
            return False
    return True
    
num_primes = 1
last_prime = 2
val_to_check = 3

while num_primes < 10001:
    
    if is_prime(val_to_check):

        if num_primes % 20 == 0:
            print(num_primes, last_prime)
        last_prime = val_to_check
        num_primes +=1
    val_to_check += 2
    
print(last_prime)    


