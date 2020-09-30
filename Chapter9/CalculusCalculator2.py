# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 23:20:31 2020

@author: lars-johan.brannmark
"""
import numpy as np
import matplotlib.pyplot as plt

from integrate import Midpoint, Trapezoidal, Simpson
from Diff import Forward1, Forward3, Backward1, Central2, Central4, Central6
from minmaxf import MinMax
from Newton import Newton

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
        
    def inverse(self, x, h=1E-6):
        def F(gamma):
            return self.f(gamma) - xi

        def dFdx(gamma):
            return (F(gamma+h) - F(gamma-h))/(2*h)
        
        g = np.zeros_like(x)
        
        for i in range(len(x)):
            xi = x[i]
            # Compute start value (use last g[i-1] if possible)
            if i == 0:
                gamma0 = x[0]
            else:
                gamma0 = g[i-1]

            gamma, n, F_value = Newton(F, gamma0, dFdx)
            g[i] = gamma
            
        return g
        
if __name__ == '__main__':
    N = 100
    a = -1.99
    b = 3.0
    x = np.linspace(a, b, 201)
    f = lambda x: np.exp(x) - 2
    c = CalculusCalculator(f, a, b)
    
    plt.figure()
    plt.plot(x, c.f(x), label='f(x)=exp(x)-2')
    plt.plot(x, c.inverse(x), label='g(x)=f_inv(x)')
    plt.plot(x, np.log(x+2),'r--', label='log(x+2)')
    plt.legend()
    