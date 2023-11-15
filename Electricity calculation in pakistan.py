# -*- coding: utf-8 -*-
"""
Created on Wed Nov 15 14:10:54 2023

@author: SOHAIL MUHAMMAD
"""

    
unit =eval(input("enter units: "))
price_slab1 = unit*7.7400
price_slab2 = (unit>=100)*18+price_slab1
price_slab3 =unit>=200+price_slab1+price_slab2
TV = 35

if (price_slab1 or price_slab2 or price_slab3):
    result = price_slab1 or price_slab2 or price_slab3
total = result
print(total)
total_with_tex = ((20/100)*total)+total+TV+8  
print('tex with tex: ', total_with_tex)
# WT = ((24/100)*total_with_tex) +total_with_tex 
# print('total with tex: ',total_with_tex, '\n', "total along with-holding tex: ", WT)