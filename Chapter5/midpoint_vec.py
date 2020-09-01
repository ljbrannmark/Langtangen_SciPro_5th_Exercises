# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:50:33 2020

@author: lars-johan.brannmark
"""

import numpy as np

def midpointint(f, a, b, n):
    s = 0.0
    h = float(b-a)/n
    for i in range(1,n+1):
        s += f(a - 0.5*h + i*h)
    return h*s
    
def midpointint_vec1(f, a, b, n):
    h = float(b-a)/n
    y = [ f(a - 0.5*h + i*h ) for i in range(1,n+1)]
    return h*sum(y)

def midpointint_vec2(f, a, b, n):
    h = float(b-a)/n
    return h*np.sum(f(a - 0.5*h + h*np.arange(1,n+1)))

#------------------------------------------------------------------------------
def test_midpointint():
    f = lambda x: 2*x
    a = 2
    b = 4
    n = 100
    I = 12.0
    
    I0 = midpointint(f, a, b, n)
    I1 = midpointint_vec1(f, a, b, n)
    I2 = midpointint_vec2(f, a, b, n)
    
    tol = 1e-12
    success = True
    msg = 'Test failed for:'
    if (abs(I - I0) > tol):
        msg += ' midpointint'
        success = False
    if (abs(I - I1) > tol):
        msg += (not success)*',' + ' midpointint_vec1'
        success = False
    if (abs(I - I2) > tol):
        msg += (not success)*',' + ' midpointint_vec2'
        success = False

    assert success, msg
    
#------------------------------------------------------------------------------
#Test block:
if __name__ == '__main__':
    test_midpointint()
    
    
