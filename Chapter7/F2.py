# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:40:28 2020

@author: lars-johan.brannmark
"""

class F(object):
    def __init__(self, a, w):
        self.a = float(a)
        self.w = float(w)
        
    def __call__(self, x):
        return self.value(x)
    
    def __str__(self):
        return 'exp(-a*x)*sin(w*x)'
        
    def value(self, x):
        a, w = self.a, self.w
        from math import exp, sin
        return exp(-a*x)*sin(w*x)
    