# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 18:10:49 2017

@author: Edward

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.


"""

def get_cycle_size(d):
    # TODO
    f = 1.0 / d
    f = str(f)
    f = f[2:]
    
    best_cycle = 0
    for start_i in range(len(f)//2 -1):
        for end_i in range(start_i+1, len(f)//2):       
            cycle_len = end_i - start_i
            
            if f[start_i:end_i] == f[end_i: end_i+cycle_len]:
                if cycle_len > best_cycle:
                    best_cycle = cycle_len
            

        
    return best_cycle
    
    
for i in range(1,100):
    cycle_length = get_cycle_size(i)
    print(i, 1/i, cycle_length)
