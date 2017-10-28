# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 20:15:37 2017

@author: Edward
"""

number_map = {
        0: '',
        1: 'one',
        2: 'two',
        3: 'three',
        4: 'four',
        5: 'five',
        6: 'six',
        7: 'seven',
        8: 'eight',
        9: 'nine',
        10: 'ten',
        11: 'eleven',
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen',
        15: 'fifteen',
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen',
        20: 'twenty',
        30: 'thirty',
        40: 'forty',
        50: 'fifty',
        60: 'sixty',
        70: 'seventy',
        80: 'eighty',
        90: 'ninety',
        100: 'onehundred',
        1000: 'onethousand'
        }

num_list = []
for i in range(1,1001):
    print(i, '', end='')
    if i in number_map:
        print(number_map[i])
        num_list.append(number_map[i])
        continue
    if i < 100:
        print(number_map[i-i%10], number_map[i%10])
        num_list.append(number_map[i-i%10]+number_map[i%10])
        continue
    if i >= 100:
        if i % 100 == 0:
            print(number_map[i//100], 'hundred')
            num_list.append(number_map[i//100] + 'hundred')
        else:    
            if i%100 in number_map:
                print(number_map[i//100], 'hundred and', number_map[i%100])
                num_list.append(number_map[i//100] + 'hundredand' + number_map[i%100])
            else:
                print(number_map[i//100], 'hundred and', number_map[i%100 - i%10], number_map[i%10])
            
                num_list.append(number_map[i//100]+'hundredand'+number_map[i%100 - i%10]+number_map[i%10])
        
print(sum([len(l) for l in num_list]))
    
    
        
    






