# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 07:48:56 2017

@author: Edward

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?


"""
import numpy as np
 
n = 20
 
mat = np.zeros((n,n), dtype=np.int64)

for i in range(n):
    mat[0,i] = i+2
    mat[i,0] = i+2
    
for col in range(1,n):
    for row in range(1,n):
        mat[row,col] = mat[row-1,col] + mat[row, col-1]