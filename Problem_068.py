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

def get_solution(array):
    if min(array[:5]) == array[0]:
        return [array[0] , array[5]  , array[6] ,
            array[1] , array[6]  , array[7] ,  
            array[2] , array[7]  , array[8] , 
            array[3] , array[8]  , array[9] , 
            array[4] , array[9]  , array[5] ]
        
    if min(array[:5]) == array[1]:
        return [
            array[1] , array[6]  , array[7] ,  
            array[2] , array[7]  , array[8] , 
            array[3] , array[8]  , array[9] , 
            array[4] , array[9]  , array[5] ,
            array[0] , array[5]  , array[6] ,]
        
    if min(array[:5]) == array[2]:
        return [
            
            array[2] , array[7]  , array[8] , 
            array[3] , array[8]  , array[9] , 
            array[4] , array[9]  , array[5] ,
            array[0] , array[5]  , array[6] ,
            array[1] , array[6]  , array[7] ,  ]
    if min(array[:5]) == array[3]:
        return [
            array[3] , array[8]  , array[9] , 
            array[4] , array[9]  , array[5] ,
            array[0] , array[5]  , array[6] ,
            array[1] , array[6]  , array[7] ,  
            array[2] , array[7]  , array[8] , ]
        
    if min(array[:5]) == array[4]:
        return [
            array[4] , array[9]  , array[5] ,
            array[0] , array[5]  , array[6] ,
            array[1] , array[6]  , array[7] ,  
            array[2] , array[7]  , array[8] , 
            array[3] , array[8]  , array[9] , ]
        
    
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
                              
                              sol = get_solution([i,j,k,l,m,n,o,p,q,r])
                              sol_s = ''.join([str(a) for a in sol])
                              if  int(sol_s)> highest and len(sol_s) ==16:
                                  print('found 1')
                                  # if len(''.join([str(a) for a in [i,j,k,l,m,n,o,p,q,r]])) == 16:
                                  #     print('found 2')
                                  highest = int(sol_s)
                                  solution = sol
    return solution
        
    

# def recursive_search(level, array=(0,1,2,3,4,5,6,7,8,9))
#     pass

if __name__ == '__main__':
    print(find_solution())

9411013635752824