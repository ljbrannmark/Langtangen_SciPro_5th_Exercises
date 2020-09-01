# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 00:06:42 2020

@author: lars-johan.brannmark
"""
import numpy as np
import matplotlib.pyplot as plt

def L_k(x, k, xp, yp):
    P = 1
    for i in range(k):
        P *= (x - xp[i]) / (xp[k] - xp[i])
    for i in range(k+1,len(xp)):
        P *= (x - xp[i]) / (xp[k] - xp[i])
    return P

def p_L(x, xp, yp):
    return sum( yp[k]*L_k(x, k, xp, yp) for k in range(len(xp)) )

def graph(f, n, xmin, xmax, resolution=1001):
    xp = np.linspace(xmin, xmax, n)
    yp = f(xp)
    xi=np.linspace(xmin, xmax, resolution)
    yi = np.array([p_L(x, xp, yp) for x in xi])
    l1 = plt.plot(xp, yp, 'o', label='Interpolation points $f(x_i)$')
    l2 = plt.plot(xi, yi, '-', label='Lagrange interpolation $p_L(x)$')    
    plt.show()
    
def test_p_L(xp, yp):
    error = sum( abs( p_L(xp[k], xp, yp) - yp[k] ) for k in range(len(xp)) )
    assert error < 1e-12

if __name__ == '__main__':
    xmin = 0
    xmax = np.pi
    n = 5
    f = lambda x: np.sin(x)     
    xp = np.linspace(xmin, xmax, n)
    yp = f(xp)
    test_p_L(xp,yp)
    graph(f, n, xmin, xmax)