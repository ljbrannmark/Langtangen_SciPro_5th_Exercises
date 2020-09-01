# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 23:13:45 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x*(12.0-x) + np.sin(np.pi*x)

def piecewise_linear_vec(x,data):
    x = np.array(x)
    y = np.zeros_like(x)
    n = len(data)-1
    y[:] = np.NaN
    # A list of conditions for when x is within the intervals specified by data
    cond = [ np.logical_and( data[i][0] <= x, x < data[i+1][0] ) for i in range(n)]
    # Define a linear function between the data points
    for i in range(n):
        y = np.where(cond[i], (data[i+1][1] - data[i][1]) / (data[i+1][0] - data[i][0]) * (x - data[i][0]) + data[i][1], y)
    return y

n = 7          # No. of intervals
m = n*100 + 1  # No. of points on the x axis
a = 0.0        # Start of x axis
b = 10.0       # End of x axis

# Array of x coordinates
x = np.linspace(a, b, m)

# Interval step size
h = (b - a) / float(n)    

# Data points for trapezoid approximation
data = [[a + i*h, f(a + i*h) ] for i in range(n+1)]

# Plot f(x)
plt.plot(x, f(x))

# Plot the piecewise linear approximation
plt.plot(x, piecewise_linear_vec(x,data), 'r--')

# Plot the side lines of the trapezoids
for i in range(n+1):
    plt.plot( [ data[i][0], data[i][0] ], [ 0, data[i][1] ], 'r--' )

# Fill the area between f(x) and its piecewise linear approximation
plt.fill_between(x, f(x), piecewise_linear_vec(x,data))

# Set axis limits and show plot
plt.axis([x[0], x[-1], 0, 40])
plt.show()

