# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 22:43:35 2020

@author: lars-johan.brannmark
"""

from Diff import *
import numpy as np
import matplotlib.pyplot as plt

class Rootfinder(object):
    def __init__(self, f, dfdx=None):
        self.f = f
        self.dfdx = dfdx if dfdx else Central2(f)
        
    def solve(self, start_values=[0], max_iter=100, tolerance=1E-6):
        self.x = start_values
        i = 0
        while abs(f(self.x[-1])) > tolerance and i < max_iter:
            self.x += self()
            i += 1
        return self.x[-1], self.f(self.x[-1]), abs(f(self.x[-1])) < tolerance, [(x, self.f(x)) for x in self.x]
            
class Newton(Rootfinder):
    def __call__(self):
        f = self.f
        dfdx = self.dfdx
        x = self.x[-1]
        return [x - f(x)/float(dfdx(x))]
    
class Bisection(Rootfinder):
    def __call__(self):
        f = self.f
        a, b, c = self.x[-3:]
        if f(a)*f(c) <= 0:
            b = c
        else:
            a = c
        return [a, b, (a+b)/2.0]
    
class Secant(Rootfinder):
    def __call__(self):
        f = self.f
        x = self.x[-2:]
        return [x[-1] - (f(x[-1]) * (x[-1] - x[-2])) / float(f(x[-1]) - f(x[-2]))]
    
    
if __name__ == '__main__':
    print 'Solving Exercise A.11 using the Rootfinder hierarchy:\n' 
    sin = np.sin
    cos = np.cos
    tanh = np.tanh
    
    print 'Input function f(x) and its derivative f\'(x):'
    f_str = raw_input('f(x) = ')
    f = lambda x: eval(f_str)
    
    df_str = raw_input('f\'(x) = ')
    if df_str == '' or df_str is None:
        df = None
    else:
        df = lambda x: eval(df_str)
    
    print '\nInput interval limits [a, b] for the Bisection method:'
    a = float(raw_input('a = '))
    b = float(raw_input('b = '))
    
    print '\nInput start values [x0, x1] for the Newton (uses x0 only) and Secant (uses x0 and x1) methods:'
    x0 = float(raw_input('x0 = '))
    x1 = float(raw_input('x1 = '))
    
    rf_n = Newton(f, df)
    rf_b = Bisection(f, df)
    rf_s = Secant(f, df)
    
    maxit = 200
    tol = 1e-9
    
    print '%s\nEquation: %s = 0\n'%('-'*50, f_str)
    print 'Newton method interations:'
    (v1, v2, v3, v4) = rf_n.solve(start_values=[x0], max_iter=maxit, tolerance=tol)
    for v in v4:
        print 'x = %g, f(x) = %g'%(v[0], v[1])
    print 'Bisection method interations:'
    (v1, v2, v3, v4) = rf_b.solve(start_values=[a, b, (a + b)/2.0], max_iter=maxit, tolerance=tol)
    for v in v4:
        print 'x = %g, f(x) = %g'%(v[0], v[1])
    print 'Secant method interations:'
    (v1, v2, v3, v4) = rf_s.solve(start_values=[x0, x1], max_iter=maxit, tolerance=tol)
    for v in v4:
        print 'x = %g, f(x) = %g'%(v[0], v[1])