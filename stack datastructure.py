# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 15:37:21 2023

@author: SOHAIL MUHAMMAD
"""

stack = []
stack.append(1)
stack.append(2)
print(stack)
stack.append('a')
stack.append('b')
stack.append('hello')
print(stack)
stack.remove('hello')
stack.append('d')
print(stack)
print(stack.pop())
print(stack)