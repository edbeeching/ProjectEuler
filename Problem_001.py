# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:37:23 2017

@author: Edward
"""

result = sum([x for x in range(1,1000) if x%3 == 0 or x%5 == 0])
print(result)
