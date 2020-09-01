# -*- coding: utf-8 -*-
"""
Created on Sat May  9 21:47:17 2020

@author: lars-johan.brannmark
"""

vertices = {1: (0,0), 2: (1,0), 3: (0,2)}

def triangle_area(v):
    return 0.5 * abs( v[2][0]*v[3][1] - v[3][0]*v[2][1] - v[1][0]*v[3][1] 
                     + v[3][0]*v[1][1] + v[1][0]*v[2][1] - v[2][0]*v[1][1] )
    
a = triangle_area(vertices)

print a