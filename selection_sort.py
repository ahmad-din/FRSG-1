# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:47:45 2023

@author: SOHAIL MUHAMMAD
"""

def selection_sort(arr):
    for i in range(0, len(arr)-1):
        curr_min_index = i
        for j in range(i+1, len(arr)):
            if arr[j]< arr[curr_min_index]:
                curr_min_index = j
                
        arr[i],arr[curr_min_index] = arr[curr_min_index],arr[i]


arr = [6,4,5,3,1,2,]
selection_sort(arr)
print(arr)

def selection(arr):
    for i in range(0, len(arr) - 1):
        cur_mini_index = i
        for j in range(i+1, len(arr)):
            if arr[j]< arr[cur_mini_index]:
                cur_mini_index = j
                
        arr[i], arr[cur_mini_index] = arr[cur_mini_index],arr[i]
arr = [6,4,5,3,1,2,]
selection(arr)
print(arr)

def sel(arr):
    for i in range(0,  len(arr) - 1):
        current_min_index = i
        for j in range(i+1, len(arr)):
            if arr[j]<arr[current_min_index]:
                current_min_index = j
        arr[i], arr[current_min_index] = arr[current_min_index], arr[i]
arr = [6,4,5,3,1,2,]
sel(arr)
print(arr)