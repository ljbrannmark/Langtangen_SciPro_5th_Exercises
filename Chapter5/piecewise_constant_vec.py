# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 23:24:17 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def piecewise_constant_vec(x,data):
    x = np.array(x)
    y = np.zeros_like(x)
    n = len(data)-1
    cond = [ np.logical_and( data[i][0] <= x, x < data[i+1][0] ) for i in range(n)]
    cond.append( data[n][0] <= x)
    y[:] = data[0][1]
    for i in range(n+1):
        y = np.where(cond[i], data[i][1], y)    
    return y

def plot_piecewise(data, xmax):
    n = len(data)-1
    xmax = max(xmax, data[n][0])
    #Plot intervals [x_0, x_1], ..., [x_n-1, x_n]
    for i in range(0, n):
        plt.plot([data[i][0], data[i+1][0]],[data[i][1], data[i][1]],'b')
    #Plot interval [x_n, xmax]
    plt.plot([data[n][0], xmax],[data[n][1],data[n][1]],'b')
    plt.show()
    
data = [(0, -1), (1, 0), (1.5, 4), (2.75, 6), (5, -3)]

x = np.linspace(-1, 8, 501)

plt.figure()
plot_piecewise(data, x[-1])
plt.plot(x, piecewise_constant_vec(x, data),'r--')
