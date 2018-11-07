# -*- coding: utf-8 -*-
"""
Created on Sun Oct 29 21:20:19 2017

@author: Edward

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""

def triangle(n):
    return int(0.5*n*(n-1))

def val(letter):
    return ord(letter) - 64

words = []

with open('p042_words.txt','r') as f:
    words = [w[1:-1] for w in f.readlines()[0].split(',')]
    
triangle_nums = set()

print(triangle(5))

for i in range(1,1000000):
    triangle_nums.add(triangle(i))
    

triangle_words = []

for word in words:
    num = 0
    
    for letter in word:
        num += val(letter)
        
    if num in triangle_nums:
        triangle_words.append(word)
        