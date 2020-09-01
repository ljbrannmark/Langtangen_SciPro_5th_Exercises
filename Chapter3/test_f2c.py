# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 00:09:39 2019

@author: larsjohan
"""

from math import *

def C(F):
    return 5.0/9*(F - 32)

def F(C):
    return 9.0/5*C + 32

def test_F_C():
    c=51
    f=97
    tol = 1e-13
    success_F_C = ( abs( C(F(c)) - c ) < tol ) and ( abs( F(C(f)) - f < tol ) )
    msg = 'Test failed for functions C(f) and F(c).'
    assert success_F_C, msg
    
test_F_C()