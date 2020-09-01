# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 22:23:48 2020

@author: lars-johan.brannmark
"""

import matplotlib.pyplot as plt

def plot_piecewise(data, xmax):
    n = len(data)-1
    xmax = max(xmax, data[n][0])
    #Plot intervals [x_0, x_1], ..., [x_n-1, x_n]
    for i in range(0, n):
        plt.plot([data[i][0], data[i+1][0]],[data[i][1], data[i][1]],'b')
    #Plot interval [x_n, xmax]
    plt.plot([data[n][0], xmax],[data[n][1],data[n][1]],'b')
    plt.show()
    
#def plot_piecewise(data, xmax):
#    x = np.zeros(2*len(data))
#    y = np.zeros(2*len(data))
#    for i, point in enumerate(data):
#        x[2*i - 1] = x[2*i] = point[0]
#        y[2*i] = y[2*i + 1] = point[1]
#    x[-1] = xmax
#    y[-1] = y[-2] = data[-1][1]
#    plt.plot(x, y)
#    plt.show()

data = [(0, -1), (1, 0), (1.5, 4)]

plt.figure()
plot_piecewise(data, 3)