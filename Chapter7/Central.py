# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 23:25:39 2020

@author: lars-johan.brannmark
"""
import sympy as sp
import numpy as np
import sys
import matplotlib.pyplot as plt

class Central(object):
    def __init__(self, f, h=1E-6):
        self.f = f
        self.h = h

    def __call__(self, x):
        f, h = self.f, self.h      # make short forms
        return (f(x + h) - f(x - h)) / float(2*h)
    
def table(f_sp, x, h=1E-5):
    x_a = x
    x = sp.Symbol('x')
    f = sp.lambdify([x], f_sp)
    df_sp = sp.diff(f_sp, x)
    df_exact = sp.lambdify([x], df_sp)
    df_computed = Central(f, h)
    print ' '*13 + 'x |' + ' '*10 + 'Error'
    print '-'*31
    for xval in x_a:
        print '%15.6f|%15.6e' %(xval, abs(df_exact(xval)-df_computed(xval)))
    
    
def test_Central():
    f = lambda x: 0.5*x**2
    df = Central(f, h=1e-3)
    x = 2
    tol = 1e-12
    success = abs(df(x) - x) < tol
    msg = 'Error in class Central.'
    assert success, msg

if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test_Central()
        x = sp.Symbol('x')
        f = 5*sp.cos(2*x) + sp.exp(-x)*sp.sin(2*x)
        print 'Testing class Central(f) for function:\n\nf(x)=%s\n' %str(f)
        table(f, np.linspace(-5, 5, 11), h=1E-6)
        