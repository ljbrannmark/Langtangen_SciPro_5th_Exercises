# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 22:27:53 2020

@author: lars-johan.brannmark
"""

class Derivative(object):
    def __init__(self, f, h=1E-5):
        self._f = f
        self._h = float(h)

    def __call__(self, x):
        f, h = self._f, self._h      # make short forms
        return (f(x+h) - f(x))/h
    
    def set_precision(self, h):
        self._h = h
        
    def get_precision(self):
        return self._h
    
def test_Derivative():
    f = lambda x: 2.0*x
    df = Derivative(f)
    prec = 1E-2
    df.set_precision(prec)
    tol = 1e-12
    error = abs(df(1.0) - 2.0)
    success = error < tol and df.get_precision() == prec
    msg = 'Error in class Central.'
    assert success, msg
    
test_Derivative()