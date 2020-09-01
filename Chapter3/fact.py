# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 21:46:37 2019

@author: larsjohan
"""

def fact(n):
    if n <=1:
        f=1
    else:
        f = 1
        while n > 1:
            f *= n
            n -= 1
    return f

def test_fact():
    # Check an arbitrary case
    n = 4
    expected = 4*3*2*1
    computed = fact(4)
    assert expected == computed
    # Check the special case
    assert fact(0) == 1
    assert fact(1) == 1
    
test_fact()