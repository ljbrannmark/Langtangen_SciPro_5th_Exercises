# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 23:51:58 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

from integrate import Midpoint, Trapezoidal, Simpson
from Diff import Forward1, Forward3, Backward1, Central2, Central4, Central6
from minmaxf import MinMax

class CalculusCalculator(object):
    def __init__(self, f, a, b, resolution=1000):
        self.f, self.a, self.b, self.n = f, a, b, resolution
        self.minmax = MinMax(self.f, self.a, self.b, self.n)
        self.set_differentiation_method(Central2)
        self.set_integration_method(Trapezoidal)
        
    def plot(self):
        plt.figure()
        x = np.linspace(self.a, self.b, self.n)
        plt.plot(x, self.f(x))
        plt.show()
        
    def plot_derivative(self):
        plt.figure()
        x = np.linspace(self.a, self.b, self.n)
        plt.plot(x, self.df(x))
        plt.show()
        
    def extreme_points(self):
        return self.minmax
    
    def set_differentiation_method(self, method, h=1E-8):
        self.df = method(self.f, h)
        
    def set_integration_method(self, method, h=1E-8):
        self.integral = method(self.a, self.b, self.n+1).integrate(self.f)
        
if __name__ == '__main__':
    exp = np.exp
    sin = np.sin
    pi = np.pi
    def f(x):
        return x**2*exp(-0.2*x)*sin(2*pi*x)
    
    c = CalculusCalculator(f, 0, 6, resolution=5000)
    c.plot()
    c.plot_derivative()
    print c.extreme_points()
  
    print 'Integral of f(x) from x=%g to x=%g: %.17g'%(c.a,c.b,c.integral)
    print 'f\'(%g) = %.17g'%(2.51, c.df(2.51))
    print 'Changing differentiation method to Central4:' 
    c.set_differentiation_method(Central4)
    print 'f\'(%g) = %.17g'%(2.51, c.df(2.51))
    print 'Changing integration method to Simpson:' 
    c.set_integration_method(Simpson)
    print 'Integral of f(x) from x=%g to x=%g: %.17g'%(c.a,c.b,c.integral)