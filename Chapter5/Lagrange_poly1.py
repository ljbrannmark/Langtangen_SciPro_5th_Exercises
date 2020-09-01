# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 22:00:21 2020

@author: lars-johan.brannmark
"""

import numpy as np

def L_k(x, k, xp, yp):
    P = 1
    for i in range(k):
        P *= (x - xp[i]) / (xp[k] - xp[i])
    for i in range(k+1,len(xp)):
        P *= (x - xp[i]) / (xp[k] - xp[i])
    return P

def p_L(x, xp, yp):
    return sum( yp[k]*L_k(x, k, xp, yp) for k in range(len(xp)) )

def test_p_L(xp, yp):
    error = sum( abs( p_L(xp[k], xp, yp) - yp[k] ) for k in range(len(xp)) )
    assert error < 1e-12
    
xp = np.linspace(0, np.pi, 5)
yp = np.sin(xp)

test_p_L(xp,yp)

x_test = 1.0
y_interp = p_L(x_test,xp,yp)
y_exact = np.sin(x_test)

interp_error = y_interp - y_exact

print "Interpolation error for sin(%.1f): %.8f"%(x_test,interp_error)