# -*- coding: utf-8 -*-
"""
Created on Tue Jun 16 23:47:42 2020

@author: lars-johan.brannmark
"""

class F(object):
    def __init__(self, a, w):
        self.a = float(a)
        self.w = float(w)
        
    def value(self, x):
        a, w = self.a, self.w
        from math import exp, sin
        return exp(-a*x)*sin(w*x)