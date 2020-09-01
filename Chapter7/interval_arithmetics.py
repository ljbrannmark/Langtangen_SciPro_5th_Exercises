# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 14:09:30 2020

@author: lars-johan.brannmark
"""


# This class is just a first attempt - see below for a class for
# real computations with interval arithmetics.

class IntervalMath(object):
    def __init__(self, lower, upper):
        self.lo = float(lower)
        self.up = float(upper)

    def __add__(self, other):
        if isinstance(other, (int, float)):
            other = IntervalMath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a + c, b + d)
    
    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        if isinstance(other, (int, float)):
            other = IntervalMath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(a - d, b - c)
    
    def __rsub__(self, other):
        return self.__sub__(other)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            other = IntervalMath(other, other)
        a, b, c, d = self.lo, self.up, other.lo, other.up
        return IntervalMath(min(a*c, a*d, b*c, b*d),
                            max(a*c, a*d, b*c, b*d))
    
    def __rmul__(self, other):
        return self.__mul__(other)

    def __div__(self, other):
        a, b, c, d = self.lo, self.up, other.lo, other.up
        # [c,d] cannot contain zero:
        if c*d <= 0:
            raise ValueError\
                  ('Interval %s cannot be denominator because '\
                   'it contains zero')
        return IntervalMath(min(a/c, a/d, b/c, b/d),
                            max(a/c, a/d, b/c, b/d))

    def __str__(self):
        return '[%g, %g]' % (self.lo, self.up)

I = IntervalMath
x = I(1, 2)
f = x/(1.0 + x)

print f

