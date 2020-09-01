# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 22:57:25 2020

@author: lars-johan.brannmark
"""

import math
class Vec2D(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vec2D):
            result = Vec2D(self.x + other.x, self.y + other.y)
        else:
            result = Vec2D(self.x + other[0], self.y + other[1])
        return result
    
    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Vec2D):
            result = Vec2D(self.x - other.x, self.y - other.y)
        else:
            result = Vec2D(self.x - other[0], self.y - other[1])
        return result
    
    def __rsub__(self, other):
        return -self + other

    def __mul__(self, other):
        if isinstance(other, Vec2D):
            result = self.x*other.x + self.y*other.y
        else:
            result = self.x*other[0] + self.y*other[1]
        return result
    
    def __rmul__(self, other):
        return self * other
        
    def __eq__(self, other):
        if isinstance(other, Vec2D):
            result = self.x == other.x and self.y == other.y
        else:
            result = self.x == other[0] and self.y == other[1]
        return result

    def __str__(self):
        return '(%g, %g)' % (self.x, self.y)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__
    
    def __neg__(self):
        return Vec2D(-self.x, -self.y) 
