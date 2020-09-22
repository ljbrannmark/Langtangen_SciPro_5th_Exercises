# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 23:02:59 2020

@author: lars-johan.brannmark
"""

class Diff(object):
    def __init__(self, f, h=1E-6):
        self.f = f
        self.h = float(h)

class Derivative(Diff):
    def __call__(self, x):
        f, h = self.f, self.h      # make short forms
        return (f(x+h) - f(x)) / h

class Central(Diff):
    def __call__(self, x):
        f, h = self.f, self.h      # make short forms
        return (f(x+h) - f(x-h)) / (2*h)
    
class Backward(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x) - f(x-h)) / h