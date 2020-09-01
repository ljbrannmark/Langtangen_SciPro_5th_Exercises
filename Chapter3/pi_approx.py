# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 00:05:56 2019

@author: larsjohan
"""

from math import pi, sqrt, sin, cos

def pathlength(x, y):
    n = len(x)-1
    L = 0
    for i in range(1,n+1):
        L += sqrt( (x[i]-x[i-1])**2 + (y[i]-y[i-1])**2 )
    return L

def pi_approx(n):
    x = [0.5*cos( (2*pi*i)/n ) for i in range(n+1)]
    y = [0.5*sin( (2*pi*i)/n ) for i in range(n+1)]
    return pathlength(x,y)

    
for k in range(2,11):
    n=2**k
    pi_computed = pi_approx(n)
    error = pi - pi_computed
    print "Approximation error, n=%.0f: %.5e" %(n,error)