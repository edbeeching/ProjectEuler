# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 16:17:55 2017

@author: Edward

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?

"""
from math import sqrt
def get_side_lengths(p):
    combs = set()
    
    for a in range(1,p):
        for b in range(a,p):
            
            c = p - a - b
            
            if (a*a + b*b == c*c):
                combs.add((min(a,b), max(a,b), c))
    return len(combs)

best_p = 0
best_combs = 0


for p in range(1,1001):
    
    num_combs = get_side_lengths(p)

    if num_combs > best_combs:
        best_combs = num_combs
        best_p = p
        print(p)
        
print(best_p)
        
                    
    
    
    
    
    
    
    


