# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 22:38:33 2020

@author: lars-johan.brannmark
"""

from math import sqrt

class Rectangle(object):
    def __init__(self, W, H, x0, y0):
        self.W, self.H, self.x0, self.y0 = W, H, x0, y0
        
    def area(self):
        return self.W*self.H
    
    def perimeter(self):
        return 2*self.W + 2*self.H
        
class Triangle(object):
    def __init__(self, v0, v1, v2):
        self.v0, self.v1, self.v2 = v0, v1, v2
        
    def area(self):
        x0, y0 = self.v0
        x1, y1 = self.v1
        x2, y2 = self.v2
        return 0.5 * abs( x1*y2 - x2*y1 - x0*y2 + x2*y0 + x0*y1 - x1*y0)
    
    def perimeter(self):
        x0, y0 = self.v0
        x1, y1 = self.v1
        x2, y2 = self.v2
        L0 = sqrt( (x1-x0)**2 + (y1-y0)**2 )
        L1 = sqrt( (x2-x1)**2 + (y2-y1)**2 )
        L2 = sqrt( (x0-x2)**2 + (y0-y2)**2 )
        return L0 + L1 + L2

def test_Rectangle():
    r = Rectangle(2.0, 3.0, 0.0, 0.0)
    area_exact = 6.0
    perimeter_exact = 10.0
    area_computed = r.area()
    perimeter_computed = r.perimeter()
    tol = 1e-14
    msg = 'Error in class Rectangle!'
    success = abs(area_exact-area_computed) < tol and \
    abs(perimeter_exact-perimeter_computed) < tol
    assert success, msg
    
def test_Triangle():
    t = Triangle((0, 0), (1, 0), (0, 2))
    area_exact = 1.0
    perimeter_exact = 3.0 + sqrt(5)
    area_computed = t.area()
    perimeter_computed = t.perimeter()
    tol = 1e-14
    msg = 'Error in class Triangle!'
    success = abs(area_exact-area_computed) < tol and \
    abs(perimeter_exact-perimeter_computed) < tol
    assert success, msg
    
test_Rectangle()
test_Triangle()
    