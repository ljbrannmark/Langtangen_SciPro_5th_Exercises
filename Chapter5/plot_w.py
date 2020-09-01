# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 22:29:15 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def w_func(x):
    cond1 = np.logical_and( 0 <= np.abs(x), np.abs(x) < 1)
    cond2 = 1 <= np.abs(x)
    y = np.zeros_like(x)
    y[cond1] = 1 - np.abs(x[cond1])
    y[cond2] = np.abs(x[cond2]) - 1
    return y

def test_w_func():
    x = np.array([-3, -1, 0, 1, 3])
    y_computed = w_func(x)
    y_exact = np.array([2, 0, 1, 0, 2])
    #
    tol = 1e-15
    success = np.max(np.abs(y_computed - y_exact)) < tol
    msg = 'Test failed for function w_func(x)'
    assert success, msg
    
test_w_func()

x = np.linspace(-3, 3, 101)
plt.figure()
plt.plot(x, w_func(x))
