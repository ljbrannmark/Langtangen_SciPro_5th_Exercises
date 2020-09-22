# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 00:01:21 2020

@author: lars-johan.brannmark
"""
from math import exp

class Diff(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
        
class Backward1(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return ( f(x) - f(x-h) ) / h

class Backward2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return ( f(x-2*h) - 4*f(x-h) + 3*f(x) ) / (2*h)
    
g = lambda t: exp(-t)
dg = lambda t:-exp(-t)

t = 0
print '%14s%14s%14s'%('h', 'error b1', 'error b2')
print '%s'%('-'*42)
for h in [2**-k for k in range(0, 15)]:
    dg_b1 = Backward1(g, h)
    dg_b2 = Backward2(g, h)
    error_b1 = dg(t) - dg_b1(t)
    error_b2 = dg(t) - dg_b2(t)
    print '%14.5e%14.5e%14.5e'%(h, error_b1, error_b2)
    
    
    
    