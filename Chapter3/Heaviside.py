# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:50:21 2019

@author: larsjohan
"""

def H(x):
    if x < 0:
        return 0
    if x >= 0:
        return 1
    
def test_H():
    success = ( H(-10)==0 ) & ( H(-10**-15)==0 ) & ( H(0)==1 ) \
            & ( H(10**-15)==1 ) & ( H(10)==1 )
    msg = 'Heaviside function H(x) failed'
    assert success, msg
    
test_H()
