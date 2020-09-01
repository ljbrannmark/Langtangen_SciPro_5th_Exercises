# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 23:01:24 2019

@author: larsjohan
"""
from math import pi, sqrt

def pathlength(x, y):
    n = len(x)-1
    L = 0
    for i in range(1,n+1):
        L += sqrt( (x[i]-x[i-1])**2 + (y[i]-y[i-1])**2 )
    return L

def test_pathlength():
    N=10
    x=[float(n)/N for n in range(N+1)]
    y=[float(n)/N for n in range(N+1)]
    L_correct=sqrt(2)
    L_computed = pathlength(x,y)
    tol=1e-14
    success = abs(L_correct - L_computed) < tol
    msg = "Test failed for function pathlength(x, y)"
    assert success, msg
    
test_pathlength()