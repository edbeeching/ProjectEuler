# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 17:33:12 2017

@author: Edward
"""

def is_palindromic_b10b2(n):
    return str(n) == str(n)[::-1] and str(bin(n))[2:] == str(bin(n))[:1:-1]
    
sum_palindromes = 0 

for i in range(1000000):
    if is_palindromic_b10b2(i):
        sum_palindromes += i
        
        
print(sum_palindromes)


