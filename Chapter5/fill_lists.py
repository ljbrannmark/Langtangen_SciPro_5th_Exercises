# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:22:47 2020

@author: lars-johan.brannmark
"""
from math import pi, exp, sqrt

def h(x):
    return 1.0/sqrt(2*pi) * exp(-1.0/2 * x**2)

n = 41
x0 = -4.0
x1 = 4.0
dx = float(x1-x0)/(n-1)

xlist = [x0 + i*dx for i in range(n)] 
hlist = [h(x) for x in xlist]