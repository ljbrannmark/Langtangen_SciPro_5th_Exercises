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
    sin = np.sin
    cos = np.cos
    tanh = np.tanh
    
    f1 = 'sin(x)'
    df1 = 'cos(x)'
    f2 = 'sin(x) - x'
    df2 = 'cos(x) - 1'
    f3 = 'sin(x) - x**5'
    df3 = 'cos(x) - 5*x**4'
    f4 = 'x**4*sin(x)'
    df4 = '4*x**3*sin(x) + x**4*cos(x)'
    f5 = 'x**4 - 16.0'
    df5 = '4*x**3'
    f6 = 'x**10 - 1'
    df6 = '10*x**9'
    f7 = 'tanh(x)'
    df7 = '1 - tanh(x)**2'
    f8 = 'tanh(x) - x**10'
    df8 = '1 - tanh(x)**2 - 10*x**9'
    
    #Collect the equations and their start values in a list of tuples:
    equations = [(f1, df1, [-4.0, -2.0], [-4.0, -3.9]),\
                 (f2, df2, [-1.0, 0.9], [-1.0, -0.9]),\
                 (f3, df3, [-1.5, 0.7], [-1.5, -1.49]),\
                 (f4, df4, [3.0, 5.0], [3.0, 3.1]),\
                 (f5, df5, [-5.0, 0.0], [-5.0, -4.9]),\
                 (f6, df6, [0.9, 1.5], [1.5, 1.51]),\
                 (f7, df7, [-1.0, 1.1], [-1.0, -0.9]),\
                 (f8, df8, [0.9, 1.5], [0.9, 0.91])]
    
    for f_str, df_str, a_b, x0_x1 in equations:
        
        f = lambda x: eval(f_str)
        df = lambda x: eval(df_str)
        
        a, b = a_b
        x0, x1 = x0_x1
        
        rf_n = Newton(f, df)
        rf_b = Bisection(f, df)
        rf_s = Secant(f, df)
        
        maxit = 200
        tol = 1e-9
        
        rf_n.solve(start_values=[x0], max_iter=maxit, tolerance=tol)
        rf_b.solve(start_values=[a, b, (a + b)/2.0], max_iter=maxit, tolerance=tol)
        rf_s.solve(start_values=[x0, x1], max_iter=maxit, tolerance=tol)
        
        print '%s\nAlgebraic equation: %s = 0'%('-'*50, f_str)
        print 'Newton method interations:'
        for x in rf_n.x:
            print 'x=%g'%x
        print 'f(x)=%g'%f(rf_n.x[-1])
        print 'Bisection method interations:'
        for x in rf_b.x:
            print 'x=%g'%x
        print 'f(x)=%g'%f(rf_b.x[-1])
        print 'Secant method interations:'
        for x in rf_s.x:
            print 'x=%g'%x
        print 'f(x)=%g'%f(rf_s.x[-1])