# -*- coding: utf-8 -*-
"""
Created on Tue May 2 20:19:33 2023

@author: jmrod
"""

for i in range (0, 1001, 2):
    if i==0:
        ai= None
    else:
        ai= ((-1) ** i) * (i ** 2 - 1) /(2*i)
        print( 'ai', i, '= ', ai)
        
        
