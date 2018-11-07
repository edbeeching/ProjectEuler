# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 10:44:33 2017

@author: Edward

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""

###  {1}, {1,2}, {1,2,5}
#1# 1
#2# 1
#3# 1
#4# 1
#5# 1
#6# 1
#7# 1
#8# 1
#9# 1

import numpy as np

coin_groups = [[1], 
               [1,2],
               [1,2,5],
               [1,2,5,10],
               [1,2,5,10,20],
               [1,2,5,10,20,50],
               [1,2,5,10,20,50,100], 
               [1,2,5,10,20,50,100, 200]]


coin_matrix = np.zeros((201, len(coin_groups)+1))

# rules
# 1 if max of group is less that or equal i, combinations = cm(i-max(group), j) + cm(i, j-1)
# if max of group is more than j, combinations = cm(i, j-1)
coin_matrix[0,:] = 1
#coin_matrix[:,0] = 1
coin_matrix[1,1] = 1
for j,group in enumerate(coin_groups, 1):
    for i in range(1, 201):
        if max(group) <= i:
            coin_matrix[i,j] = coin_matrix[i-max(group),j] + coin_matrix[i, j-1]
        else:
            coin_matrix[i,j] = coin_matrix[i,j-1]
        
        


















    