# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:37:24 2020

@author: lars-johan.brannmark
"""

from math import *

class Backward(object):
    def __init__(self, f, h=1e-9):
        self.f, self.h = f, h
    def __call__(self, x):
        h, f = self.h, self.f
        return (f(x) - f(x-h))/h
    
dsin = Backward(sin)
e = dsin(0) - cos(0); print 'error:', e
dexp = Backward(exp, h=1e-7)
e = dexp(0) - exp(0); print 'error:', e