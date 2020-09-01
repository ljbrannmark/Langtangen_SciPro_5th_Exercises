# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 22:05:37 2020

@author: lars-johan.brannmark
"""

import numpy as np

#Define 'scalar' version of polygon area function, same as in Exercise 3.19:
def polygon_area(x, y):
    A=0
    for i in range(len(x)):
        A += x[i-1]*y[i] - y[i-1]*x[i]
    return 0.5*A

#Define a vectorized version:
def polygon_area_1(x, y):
   return 0.5*np.abs(np.dot(x[:-1],y[1:]) + x[-1]*y[0] 
                     - np.dot(y[:-1],x[1:]) + x[0]*y[-1]) 

   
def test_polygon_area_1():
    x = np.array([0, 2, 2, 1, 0])
    y = np.array([0, 0, 2, 3, 2])
    A = polygon_area(x, y)
    A1 = polygon_area_1(x, y)
    success = A == A1
    msg = 'Test failed: Polygon area functions are not equal'
    assert success, msg
    
test_polygon_area_1()