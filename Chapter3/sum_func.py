# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 00:11:19 2019

@author: larsjohan
"""

def sum_1k(M):
    s = 0
    for i in range(1, M+1):
        s += 1.0/i
    return s
        
def test_sum_1k():
    correct = 11.0/6
    computed = sum_1k(3)
    tol = 1E-14
    success = abs(correct-computed) < tol
    msg = 'Function sum_1k() failed test'
    assert success, msg
    
test_sum_1k()
