# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:28:02 2020

@author: lars-johan.brannmark
"""

class Derivative(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h      # make short forms
        return (f(x+h) - f(x))/h