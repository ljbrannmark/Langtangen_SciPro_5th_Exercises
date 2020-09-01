# -*- coding: utf-8 -*-
"""
Created on Mon Jul  6 00:03:03 2020

@author: lars-johan.brannmark
"""

from Heaviside_class import Heaviside
import numpy as np
import matplotlib.pyplot as plt

class Indicator(object):
    
    def __init__(self, L, R, eps=None):
        self.L = L
        self.R = R
        self.eps = eps
    
    def __call__(self, x):
        L, R, eps = self.L, self.R, self.eps
        H = Heaviside(eps)
        return H(x-L)*H(R-x)
    
    def plot(self, xmin, xmax, n):
        x = np.linspace(xmin, xmax, n)
        plt.figure()
        plt.plot(x, self(x))
        plt.axis([xmin, xmax, -0.1, 1.1])
        plt.title('Indicator function I(x)')
        plt.xlabel('x')
        plt.ylabel('y = I(x)')
        plt.show()