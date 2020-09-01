# -*- coding: utf-8 -*-
"""
Created on Wed Sep 11 23:19:57 2019

@author: larsjohan
"""

from math import cos, pi

def maxmin(f, a, b, n=1000):
    h = (b - a) / float(n - 1)
    x = []
    y = []
    for i in range(n):
        x.append(a + i*h)
        y.append( f(x[i]) )
    ymax=max(y)
    ymin=min(y)
    return ymax, ymin

def test_maxmin():
    f = lambda x: cos(x)
    ymax_expected = 1.0
    ymin_expected = -1.0
    tol = 1E-5
    ymax, ymin = maxmin(f, -pi/2.0, 2.0*pi, 1000)
    success = ( abs(ymax - ymax_expected) < tol ) & ( abs(ymin - ymin_expected) < tol )
    msg = 'Function maxmin failed!'
    assert success, msg

test_maxmin()