# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 22:26:17 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(12.0-x) + np.sin(np.pi*x)

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

n = 7
m = n*100 + 1
a = 0.0
b = 10.0
x = np.linspace(a, b, m)

h = (b - a) / float(n)
data = [(i*h, f(a + i*h + 0.5*h) ) for i in range(n)]

plt.plot(x, f(x))
plt.plot(x, piecewise_constant_vec(x,data), 'r--')
for i in range(n):
    plt.plot( [ data[i][0], data[i][0] ], [ 0, data[i][1] ], 'r--' )
plt.fill_between(x, f(x), piecewise_constant_vec(x,data))
plt.axis([0, 10, 0, 40])
plt.show()