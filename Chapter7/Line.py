# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 22:52:10 2020

@author: lars-johan.brannmark
"""

class Line(object):
    def __init__(self, p1, p2):
        self.x0, self.y0 = p1
        self.x1, self.y1 = p2
    
    def value(self, x):
        x0, y0 = self.x0, self.y0
        x1, y1 = self.x1, self.y1
        a = (y1 - y0)/float(x1 - x0)
        b = y0 - a*x0
        return a*x + b
    
def test_Line():
    p1 = (0, 1)
    p2 = (4, 9)
    l = Line(p1, p2)
    x = 2
    y_exact = 5.0
    y_computed = l.value(x)
    tol = 1e-14
    msg = 'Error in class Line.'
    success = abs(y_exact - y_computed) < tol
    assert success, msg