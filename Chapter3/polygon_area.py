# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 00:37:32 2019

@author: larsjohan
"""

from math import sqrt, cos, sin, pi

def polygon_area(x, y):
    A=0
    for i in range(len(x)):
        A += x[i-1]*y[i] - y[i-1]*x[i]
    return 0.5*A

x_triangle = [-1, 1, 0]
y_triangle = [0, 0, 2]

x_quad = [0, 5, 5, 0]
y_quad = [0, 0, 2, 2]

x_penta = [cos( (2*pi*i)/5 ) for i in range(5)]
y_penta = [sin( (2*pi*i)/5 ) for i in range(5)]

A_triangle_true = 2.0
A_quad_true  = 10.0
A_penta_true  = 5.0/4*sqrt( (5+sqrt(5))/2)

A_triangle_computed = polygon_area(x_triangle, y_triangle)
A_quad_computed  = polygon_area(x_quad, y_quad)
A_penta_computed  = polygon_area(x_penta, y_penta)