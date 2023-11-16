# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 10:40:11 2023

@author: SOHAIL MUHAMMAD
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1]>arr[j] and j>0:
            arr[j - 1], arr[j] = arr[j], arr[j - 1]
            j -= 1
            
arr = [5,4,3,2,1,8,7,6]
insertion_sort(arr)
print(arr)

def insertion(arr):
    for i in range(1, len(arr)):
        j = i
        while arr[j - 1]>arr[j] and j>0:
            arr[j - 1], arr[j] = arr[j], arr[j -1]
            j-=1
arr = [9,8,7,6,5,4,3,2]