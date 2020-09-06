# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 00:14:41 2020

@author: lars-johan.brannmark
"""

from math import sin, cos, sqrt,pi

class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
        
    def __str__(self):
        return 'x=%g, y=%g' %(self.x, self.y)
    
class PolarPoint(Point):
    def __init__(self, r, theta):
        self.r, self.theta = r, theta
        Point.__init__(self, r*cos(theta), r*sin(theta))
        
    def __str__(self):
        return 'r=%g, theta=%g, x=%g, y=%g' %(self.r, self.theta, self.x, self.y)
    
def test_PolarPoint():
    p1 = PolarPoint(2.0, pi/4)
    p2 = PolarPoint(3.0, pi/2)
    tol = 1E-15
    msg = 'Error in class PolarPoint'
    success = True
    success = \
    abs(p1.x-sqrt(2.0)) < tol and\
    abs(p1.y-sqrt(2.0)) < tol and\
    abs(p1.r-2.0) < tol and\
    abs(p1.theta-pi/4.0) < tol and\
    abs(p2.x) < tol and\
    abs(p2.y-3.0) < tol and\
    abs(p2.r-3.0) < tol and\
    abs(p2.theta-pi/2.0) < tol
    assert success, msg

test_PolarPoint()


