# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 17:13:56 2017

@author: Edward

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""

import math
def get_divisors(num):
    divs = set()
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            divs.add(i)
            divs.add(num//i)
    return sorted(list(divs))

abundant_nums = set()

for n in range(2, 28124):
    divs = get_divisors(n)[:-1]
    if sum(divs) > n:
        abundant_nums.add(n)
    
abundant_nums_list = list(abundant_nums)
total = 0

for n in range(1,28124):
    not_abundant = True
    for num in abundant_nums_list:
        if n - num in abundant_nums:
            not_abundant = False
            continue
        
    if not_abundant:
        total += n

print(total)
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            