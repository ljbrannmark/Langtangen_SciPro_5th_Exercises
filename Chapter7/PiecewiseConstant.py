# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 23:15:59 2020

@author: lars-johan.brannmark
"""
import numpy as np
import matplotlib.pyplot as plt

class PiecewiseConstant(object):
    
    def __init__(self, data, xmax):
        self.data, self.xmax = data, xmax

    def __call__(self, x):
        data, xmax = self.data, self.xmax
        y = np.NaN
        for v, xi in data:
            y = np.where( np.logical_and(xi <= x, x <= xmax), v, y )
        return y
    
    def plot(self):
        data, xmax = self.data, self.xmax
        #Repeat the last y value at xmax, to complete the last interval
        data.append((data[-1][0], xmax))  
        n = len(data)
        # x = [x0, x1, x1, x2, x2, x3, ...]
        # y = [y0, y0, y1, y1, y2, y2, ...]
        x = [data[i][1] for j in zip(range(0,n-1),range(1,n))   for i in j]
        y = [data[i][0] for j in zip(range(0,n-1),range(0,n-1)) for i in j]
        return x, y
    
f = PiecewiseConstant([(0.4, 1), (0.2, 1.5), (0.1, 3)], xmax=4)
print f(1.5), f(1.75), f(4)

x = np.linspace(0, 4, 21)
print f(x)

x, y = f.plot()
plt.plot(x, y)