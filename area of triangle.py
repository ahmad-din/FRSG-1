# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 15:45:12 2023

@author: SOHAIL MUHAMMAD
"""
from math import sqrt
def area_of_triangle(a,b,c):
    s = (a+b+c)/2
    A = sqrt(s*(s-a)*(s-c)*(s-c))
    return A

a,b,c = eval(input('Enter the values of first triangle: '))
A1 = area_of_triangle(a, b, c)

a,b,c = eval(input('Enter the values of second triangle: '))
A2 = area_of_triangle(a, b, c)

a,b,c = eval(input('Enter the values of third triangle: '))
A3 = area_of_triangle(a, b, c)

print(f'the area of {A1} , {A2} and {A3}')