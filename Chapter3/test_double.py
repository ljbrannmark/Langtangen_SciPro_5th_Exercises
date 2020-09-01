# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 00:03:49 2019

@author: larsjohan
"""

def double(x):
    return 2*x

def test_double():
    assert double(2) == 4
    assert abs(double(0.1) - 0.2) < 1E-15
    assert double([1, 2]) == [1, 2, 1, 2]
    assert double((1, 2)) == (1, 2, 1, 2)
    assert double(3+4j) == 6+8j
    assert double('hello') == 'hellohello'
    
test_double()