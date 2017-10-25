# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 07:48:56 2017

@author: Edward

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?


"""

import numpy as np




def gen_paths(n):
    paths = set()
    first_path = [1]*n + [0]*n
    
    
n = 5
first_path = [1]*n + [0]*n

permute = np.random.permutation(first_path)
np.array_str(permute)
