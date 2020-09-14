# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 17:17:21 2020

@author: lars-johan.brannmark
"""
from math import sin, cos, pi

class FuncWithDerivatives(object):
    def __init__(self, h=1.0E-9):
        self.h = h  # spacing for numerical derivatives
    def __call__(self, x):
        raise NotImplementedError('___call__ missing in class %s' %
                                  self.__class__.__name__)
    def df(self, x):
        """Return the 1st derivative of self.f."""
        # Compute first derivative by a finite difference
        h = self.h
        return (self(x+h) - self(x-h))/(2.0*h)

    def ddf(self, x):
        """Return the 2nd derivative of self.f."""
        # Compute second derivative by a finite difference
        h = self.h
        return (self(x+h) - 2*self(x) + self(x-h))/(float(h)**2)
    
class Sine1(FuncWithDerivatives):
    def __call__(self, x):
        return sin(x)
    
class Sine2(FuncWithDerivatives):
    def __call__(self, x):
        return sin(x)
    
    def df(self, x):
        return cos(x)
        
    def ddf(self, x):
        return -sin(x)
    
X = [0.0, pi/2]

for x in [0.0, pi/4]:
    for h in [1.0E-9, 1.0E-3]:
        sin1 = Sine1(h)
        sin2 = Sine2(h)
        print 'x=%g, h=%g:'%(x, h)
        print 'sin1.df(x)=%.10g, sin2.df(x)=%.10g, error=%g'%(sin1.df(x), sin2.df(x), sin1.df(x)-sin2.df(x))
        print 'sin1.ddf(x)=%.10g, sin2.ddf(x)=%.10g, error=%g\n'%(sin1.ddf(x), sin2.ddf(x), sin1.ddf(x)-sin2.ddf(x))
    
    
    
    