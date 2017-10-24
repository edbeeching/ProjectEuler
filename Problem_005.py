# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:21:00 2017

@author: Edward


2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


def check_val(val):
    for i in range(1,21):
        if val % i != 0:
            return False
    return True


all_vals= [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
primes = [3,5,7,11,13,17,19]
step_size=1

for p in primes:
    step_size*=p

total=1
for val in all_vals[::-1]:
    total *= val
    
smallest  = total
for i in range(step_size, total+step_size, step_size):
    if check_val(i):
        smallest = i
        break
    
print(smallest)
    












