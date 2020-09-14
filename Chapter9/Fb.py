# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 21:35:26 2020

@author: lars-johan.brannmark
"""

from numpy import exp, sin

class F(object):
    def __init__(self, a, b):
        self.a, self.b = a, b
        
    def __call__(self, t):
        return exp(-self.a*t)*sin(self.b*t)
    
class Fb(F):
    def __init__(self, a, t):
        self.a, self.t = a, t
        
    def __call__(self, b):
        self.b = b
        return F.__call__(self, self.t)
    
f = Fb(t=2, a=4.5)
print f(3)