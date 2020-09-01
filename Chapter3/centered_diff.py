# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:17:06 2019

@author: larsjohan
"""

from math import exp, cos, log, pi

def diff(f, x, h=1E-5):
    df = ( f(x + h) - f(x - h) ) / ( 2*float(h) )
    return df

def test_diff():
    tol = 1E-9
    f = lambda x: x**2 + 3*x - 1
    x = 2.0
    h=1E-4
    df_exact = 2*x + 3
    df_computed = diff(f, x, h)
    success = abs( df_exact - df_computed ) < tol
    msg = 'function diff(f, x, h) failed'
    assert success, msg
    
test_diff()

f1 = lambda x: exp(x)
x = 0
df1 = diff(f1, x, h = 0.01)

f2 = lambda x: exp(-2.0*x**2)
x = 0
df2 = diff(f2, x, h = 0.01)

f3 = lambda x: cos(x)
x = 2*pi
df3 = diff(f3, x, h = 0.01)

f4 = lambda x: log(x)
x = 1
df4 = diff(f4, x, h = 0.01)