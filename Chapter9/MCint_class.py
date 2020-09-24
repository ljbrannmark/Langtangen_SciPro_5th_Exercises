# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 18:06:17 2020

@author: lars-johan.brannmark
"""
import numpy as np
import math

from integrate import Integrator

#Add subclass MCint to the Integrator hierarchy
class MCint(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n
        h = (b-a)/float(n)
        x = np.random.uniform(a, b, n)
        w = np.zeros(len(x)) + h
        return x, w

def test_MCint():
    def f(x):
        return x + 2
    def F(x):
        return x**2/2.0 + 2*x
    
    x0 = 0.0
    x1 = 1.0
    
    np.random.seed(0)
    i = MCint(x0, x1, 3)
    
    x = i.points
    I_manual = (f(x[0]) + f(x[1]) + f(x[2])) / 3.0
    I_computed = i.integrate(f)
    print 'Manual calculation: %.18f'%I_manual
    print 'Using class MCint: %.18f'%I_computed
    print 'Error = %e'%(I_manual-I_computed)
    
    np.random.seed(0)
    i_exact = F(x1) - F(x0)
    error = {}
    for n in [10**k for k in [3, 4, 5, 6]]:
        i_mc = MCint(x0, x1, n)
        error[n] = i_exact - i_mc.integrate(f)
    print '\nError of MCint as a function of n:'
    for key in sorted(error.keys()):
        print 'n=%d: error=%g'%(key, error[key])
    
test_MCint()