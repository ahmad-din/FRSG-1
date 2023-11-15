# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 12:17:05 2023

@author: SOHAIL MUHAMMAD
"""

def fun(n):
    if n==0 or n==1:
        return 1
    else:
       val = n*fun(n-1)
    return val
        
fun(4)