# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 22:24:41 2019

@author: larsjohan
"""

def L3(x, epsilon=1.0E-6):
    x = float(x)
    i = 1
    term = (1.0/i)*(x/(1+x))**i
    s = term
    while abs(term) > epsilon:
        i += 1
        term = (1.0/i)*(x/(1+x))**i
        s += term
    return s, i

def L3_ci(x, epsilon=1.0E-6):
    i = 1
    term = x/(1.0+x)
    s = term
    while abs(term) > epsilon:
        i += 1
        term = term*( (i-1.0)/i * x/(1.0+x) )
        s += term
    return s, i

def test_L3_ci():
    x = 45.5
    eps = 1.0E-12
    s1, i1 = L3(x, eps)
    s2, i2 = L3_ci(x, eps)
    success = (abs(s1-s2) < eps/10 ) & (i1 == i2)
    msg = 'Function L3_ci failed!'
    assert success, msg
    
test_L3_ci()