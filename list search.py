# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 14:13:05 2023

@author: SOHAIL MUHAMMAD
"""

l = [1,2,3,4,5]
i = 4
index_i = l.index(i)
if i in l:
    print('the value exists','\n','the index of i is: ',index_i, end = ' ')
else:
    print('sorry')