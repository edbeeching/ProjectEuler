# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 10:44:33 2017

@author: Edward
"""
import math
def get_divisors(num):
    divs = set()
    for i in range(1,int(math.sqrt(num))+1):
        if num % i == 0:
            divs.add(i)
            divs.add(num//i)
    return sorted(list(divs))

def check_pandigital(n):

    divisors = get_divisors(n)[1:-1]
    
    num_divisors = (len(divisors)+1) // 2
    for i in range(num_divisors):
        found = True
        
        vals = set([1,2,3,4,5,6,7,8,9])
        for v in str(n):
            if int(v) not in vals:
                return False #  Dupicate entry                
            vals.remove(int(v))        
        first = divisors[i]
        second = divisors[-(1+i)]
        
        for v in str(first):
            if int(v) not in vals:
                found = False
                continue
            else:
                vals.remove(int(v))
        
        for v in str(second):
            if int(v) not in vals:
                found = False
                continue
            else:
                vals.remove(int(v))        
        if found and len(vals) == 0:
            return True
    return False

sum_pang= 0

for i in range(1,100000):
    if check_pandigital(i):
        print(i)
        sum_pang += i

print(sum_pang)


import itertools

values = [1,2,3,4,5,6,7,8,9]

collected = set()

for i in range(1,10):
    for permute in itertools.permutations(values,i):
        p_val1 = sum([a*10**b for b,a in enumerate(permute)])
        
        rest = set(values)
        for p in permute:
            rest.remove(p)

        for j in range(1, len(rest)-1):
            for permute2 in itertools.permutations(rest,j):
                p_val2 = sum([a*10**b for b,a in enumerate(permute2)])
                
                result = p_val1*p_val2
                combined = sorted([int(t) for t in (str(result)+str(p_val1)+str(p_val2))])
                #print(p_val1, p_val2, result)
                
                if combined == values:
                    print(result)
                    collected.add(result)
                

print(sum([r for r in collected]))


