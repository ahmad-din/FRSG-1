# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 14:12:37 2023

@author: SOHAIL MUHAMMAD
"""

def bubble(arr):
    for i in range(0, len(arr)-1):
        for j in range(0, len(arr)-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1], arr[j]
                
arr = [6,4,5,3,1,2,]
bubble(arr)
print(arr)