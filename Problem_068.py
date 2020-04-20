#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 11:44:50 2020

@author: edward

Magic 5-gon ring

"""
import numpy as np
import matplotlib.pyplot as plt

import torch
from torch import nn
import torch.nn.functional as F


def check_ring(array):
    return (
        array[0] + array[5]  + array[6] ==  
        array[1] + array[6]  + array[7] ==  
        array[2] + array[7]  + array[8] ==  
        array[3] + array[8]  + array[9] ==  
        array[4] + array[9]  + array[5]   
        )
    
    
def find_solution():
    
    highest = 0
    solution = ''
    for i in range(1,11):
      for j in set(range(1,11)).difference([i]):
        for k in set(range(1,11)).difference([i,j]):
          for l in set(range(1,11)).difference([i,j,k]):
            for m in set(range(1,11)).difference([i,j,k,l]):
              for n in set(range(1,11)).difference([i,j,k,l,m]):
                for o in set(range(1,11)).difference([i,j,k,l,m,n]):
                  for p in set(range(1,11)).difference([i,j,k,l,m,n,o]):
                    for q in set(range(1,11)).difference([i,j,k,l,m,n,o,p]):
                      for r in set(range(1,11)).difference([i,j,k,l,m,n,o,p,q]):
                          if check_ring([i,j,k,l,m,n,o,p,q,r]):
                              if int(''.join([str(a) for a in [i,j,k,l,m,n,o,p,q,r]])) > highest:
                                  print('found 1')
                                  # if len(''.join([str(a) for a in [i,j,k,l,m,n,o,p,q,r]])) == 16:
                                  #     print('found 2')
                                  highest = int(''.join([str(a) for a in [i,j,k,l,m,n,o,p,q,r]]))
                                  solution = [i,j,k,l,m,n,o,p,q,r]
    return solution
        
    

# def recursive_search(level, array=(0,1,2,3,4,5,6,7,8,9))
#     pass

if __name__ == '__main__':
    print(find_solution())
