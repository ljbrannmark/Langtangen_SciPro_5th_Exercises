# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 00:03:17 2020

@author: lars-johan.brannmark
"""

class Line(object):
    def __init__(self, p1, p2):
        if isinstance(p1, (tuple,list)) and isinstance(p2, (tuple,list)):
            x0, y0 = p1
            x1, y1 = p2
            self.a = (y1 - y0)/float(x1 - x0)
            self.b = y0 - self.a*x0
        elif isinstance(p1, (tuple,list)) and isinstance(p2, (float,int)):
            self.a = float(p2)
            self.b = p1[1] - p2*p1[0]
        elif isinstance(p1, (float,int)) and isinstance(p2, (float,int)):
            self.a = p1
            self.b = p2
    
    def value(self, x):
        return self.a*x + self.b
    
def test_Line():
    #Test two points as input
    p1 = (0, 1)
    p2 = (4, 9)
    l = Line(p1, p2)
    x = 2
    y_exact = 5.0
    y_computed = l.value(x)
    tol = 1e-14
    success1 = abs(y_exact - y_computed) < tol
    #Test point and slope as input
    p1 = (0, 1)
    p2 = 2
    l = Line(p1, p2)
    x = 2
    y_exact = 5.0
    y_computed = l.value(x)
    tol = 1e-14
    success2 = abs(y_exact - y_computed) < tol
    #Test slope and y-axis intersection as input
    p1 = 2
    p2 = 1
    l = Line(p1, p2)
    x = 2
    y_exact = 5.0
    y_computed = l.value(x)
    tol = 1e-14
    success3 = abs(y_exact - y_computed) < tol
    success = success1 and success2 and success3
    msg = 'Error in class Line.'
    assert success, msg