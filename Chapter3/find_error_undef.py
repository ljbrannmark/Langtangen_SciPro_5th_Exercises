# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:24:54 2019

@author: larsjohan
"""
from math import exp, sin

def expsin(x, p, q):
    return exp(p*x)*sin(q*x)

def f(x, m, n, r, s):
    return expsin(x, r, m) + expsin(x, s, n)

x = 2.5
print f(x, 0.1, 0.2, 1, 1)
