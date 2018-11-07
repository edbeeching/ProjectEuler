# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 09:48:00 2017

@author: Edward

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.


"""
import itertools

def check_divisble(n):
    if len(str(n)) < 10: return False
    
    check_vals = [2,3,5,7,11,13,17]
    n_string = str(n)
    for i,v in enumerate(range(1,8)):
        if int(n_string[v:v+3]) % check_vals[i] !=0:
            return False
        
    return True
  
total = 0
for permute in itertools.permutations([0,1,2,3,4,5,6,7,8,9]):
    val = sum([a*10**b for b,a in enumerate(permute)])
    if check_divisble(val):
        print(val)
        total += val


print(total)




# There is a much more efficient way to do this, find permutations with d2d3d5 divisible by 2, then find d3d4d5 etc