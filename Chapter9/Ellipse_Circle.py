# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 00:06:04 2020

@author: lars-johan.brannmark
"""
from math import pi, sqrt
from scipy.special import ellipe

class Ellipse(object):
    def __init__(self, x0, y0, R1, R2):
        self.x0, self.y0, self.R1, self.R2 = x0, y0, R1, R2

    def area(self):
        return pi*self.R1*self.R2
    
    def circumference(self):
        a = float(max(self.R1, self.R2))
        b = float(min(self.R1, self.R2))
        e_sq = 1.0 - b**2/a**2   # eccentricity squared
        c = 4.0*a*ellipe(e_sq)   # circumference formula
        return c

class Circle(Ellipse):
    def __init__(self, x0, y0, R):
        Ellipse.__init__(self, x0, y0, R, R)
    
e = Ellipse(2, 2, 4, 6)
c = Circle(2, 2, 4)

print e.circumference()
print c.circumference()

print e.area()
print c.area()