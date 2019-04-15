#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 12 10:40:48 2019

@author: edward

Diophantine equation

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.


"""
import math

def calc_y(x, D):
    return math.sqrt((x**2 -1)/D)
    
def is_whole(y):
    return y // 1 == y

def is_valid(x, D):
    y = calc_y(x, D)
    return is_whole(y)
    
def is_square(x):
    return is_whole(math.sqrt(x))

def diophantine_minimal_solution(D):
    x = 2
    while True:
        if is_valid(x,D):
            return x
        x += 1
        
        
def calc_x(y, D):
    return math.sqrt(1+D*y**2)
        
def is_valid_y(y, D):
    x = calc_x(y, D)
    return is_whole(x)       
 
def diophantine_minimal_solution2(D):
    y = 1
    while True:
        if is_valid_y(y,D):
            return y
        y += 1

def get_x(y, D):
    return calc_x(y, D)

def min_sol_ping_pong(D):
    # return the x solution
    x = 2
    while True:
        y = calc_y(x, D)
        if is_whole(y):
            return x
        y = math.ceil(y)
        x = calc_x(y, D)
        if is_whole(x):
            return x
        x = math.ceil(x)
        print(x,y)
        

def min_sol_ping_pong2(D):
    
    xsq = 2**2
    
    while True:
        
        ysq = (xsq-1)/D
        print(math.sqrt(xsq), math.sqrt(ysq))
        y = math.sqrt(ysq)
        if is_whole(y):
            return math.sqrt(xsq)
        y = math.ceil(y)
        ysq = y**2
        xsq = D*ysq + 1
        
        #xsq = math.ceil(xsq)
        x = math.sqrt(xsq)
        x = math.ceil(x)
        xsq = x**2
        
        #print(math.sqrt(xsq))
        
def min_sol_ping_pong3(D):
    ysq = 1
    
    while True:
        xsq = D*ysq + 1
        #print(math.sqrt(xsq), math.sqrt(ysq))
        x = math.sqrt(xsq)
        if is_whole(x):
            return x
        x = math.ceil(x)
        xsq = x**2
        
        ysq = (xsq-1)/D
        ysq = math.ceil(ysq)
        
        y = math.sqrt(ysq)
        ysq = math.ceil(y)**2
        


if __name__ == '__main__':

    # sol_y = diophantine_minimal_solution2(61)
    # sol_x = get_x(sol_y, 61)
    #sol_x = min_sol_ping_pong3(61)
    for d in range(2,62):
        if is_square(d):
            continue
        print('checking for D={}'.format(d))
        sol_x = min_sol_ping_pong3(d)
        print('Solution D={} x={}'.format(d, sol_x))
    assert 0
    
    largest_x = 0 
    largest_d = 0
    for d in range(2,1000):
        if is_square(d):
            continue
        sol_y = min_sol_ping_pong3(d)
        sol_x = get_x(sol_y, d)
        print('Solution D={} x={}'.format(d, sol_x))
        
        if sol_x > largest_x:
            largest_x = sol_x
            largest_d = d
        
    
    
    


