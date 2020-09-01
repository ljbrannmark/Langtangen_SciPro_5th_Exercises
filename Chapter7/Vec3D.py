# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 23:41:48 2020

@author: lars-johan.brannmark
"""

import math
class Vec3D(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Vec3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vec3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y + self.z*other.z

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __str__(self):
        return '(%g, %g, %g)' % (self.x, self.y, self.z)

    def __abs__(self):
        return math.sqrt(self.x**2 + self.y**2 + self.z**2)

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__
    
    def cross(self, other):
        x1, y1, z1 = self.x, self.y, self.z
        x2, y2, z2 = other.x, other.y, other.z
        return Vec3D(y1*z2 - z1*y2, z1*x2 - x1*z2, x1*y2 - y1*x2)
