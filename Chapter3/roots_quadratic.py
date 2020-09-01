# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 21:29:26 2019

@author: larsjohan
"""
from math import sqrt

def roots(a, b, c):
    s=b**2 - 4*a*c
    if s < 0:
        r = 1j*sqrt(-s)
    else:
        r = sqrt(s)
    x1 = (-b + r)/(2*a)
    x2 = (-b - r)/(2*a)
    return x1, x2
    

def test_roots_float():
    r1_exact=1.0
    r2_exact=-4.0
    
    r1_computed, r2_computed = roots(1.0, 3.0, -4.0)
    
    success = r1_exact == r1_computed and r2_exact == r2_computed
    msg = 'Function roots(a, b, c) failed test'
    
    assert success, msg
    
def test_roots_complex():
    c1_exact=2.0+3.0j
    c2_exact=2.0-3.0j
    
    c1_computed, c2_computed = roots(1.0, -4.0, 13.0)
    
    success = c1_exact == c1_computed and c2_exact == c2_computed
    msg = 'Function roots(a, b, c) failed test'
    
    assert success, msg
    
test_roots_float()
test_roots_complex()
