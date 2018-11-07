# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 18:44:31 2017

@author: Edward


The sum of the squares of the first ten natural numbers is,

1^2 + 2^2 + ... + 10^2 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


"""

def diff_of_sum_of_square(number):
    sum_of_values = sum([i for i in range(number+1)])
    sum_of_squares = sum([i*i for i in range(number+1)])
    return sum_of_values*sum_of_values - sum_of_squares

print(diff_of_sum_of_square(100))
    
    





