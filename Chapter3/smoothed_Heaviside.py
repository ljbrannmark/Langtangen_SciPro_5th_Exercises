# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 23:16:00 2019

@author: larsjohan
"""

from math import sin, pi

def H_eps(x, eps=0.01):
    if x < -eps:
        return 0
    if -eps <= x <= eps:
        return 0.5 + x/(2.0*eps) + 1/(2*pi)*sin(pi*x/eps)
    if x > eps:
        return 1
    
def test_H_eps():
    eps = 1E-9
    tol=1E-15
    Hm10 = 0
    Hmeps = 0
    H0 = 0.5
    Heps = 1
    H10 = 1
    
    success = True
    success = success & ( H_eps(-10,eps)==Hm10 )
    success = success & ( abs( H_eps(-eps,eps) - Hmeps ) < tol )
    success = success & ( H_eps(0,eps)==H0 )
    success = success & ( abs( H_eps(eps,eps) - Heps ) < tol )
    success = success & ( H_eps(10,eps)==H10 )
    msg = 'Smoothed Heaviside function H_eps(x) failed'
    assert success, msg
    
test_H_eps()