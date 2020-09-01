# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:59:03 2020

@author: lars-johan.brannmark
"""


import numpy as np
import matplotlib.pyplot as plt

class LagrangeInterpolation(object):
    def __init__(self, arg1, arg2, arg3=None):
        if isinstance(arg1, np.ndarray) and isinstance(arg2, np.ndarray): 
            self.xp, self.yp = arg1, arg2
        elif callable(arg1) and isinstance(arg2, (list,tuple)) and isinstance(arg3, int):
            f, x, n = arg1, arg2, arg3
            self.xp = np.linspace(x[0], x[1], n)
            self.yp = f(self.xp)
        
    def __call__(self, x):
        return self.p_L(x)
    
    def L_k(self, x, k):
        xp, yp = self.xp, self.yp
        P = 1
        for i in range(k):
            P *= (x - xp[i]) / float(xp[k] - xp[i])
        for i in range(k+1,len(xp)):
            P *= (x - xp[i]) / float(xp[k] - xp[i])
        return P

    def p_L(self, x):
        xp, yp = self.xp, self.yp
        return sum( yp[k]*self.L_k(x, k) for k in range(len(xp)) )

    def plot(self, resolution=1001):
        xp, yp = self.xp, self.yp
        xi = np.linspace(xp[0], xp[-1], resolution)
        yi = np.array([self(x) for x in xi])
        l1 = plt.plot(xp, yp, 'o', label='Interpolation points $f(x_i)$')
        l2 = plt.plot(xi, yi, '-', label='Lagrange interpolation $p_L(x)$')
        plt.legend()
        plt.show()