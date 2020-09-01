# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 22:20:25 2020

@author: lars-johan.brannmark
"""

class Sum(object):
    
    def __init__(self, term, M, N):
        self.term = term
        self.M = M
        self.N = N
        
    def __call__(self, x):
        term = self.term
        M = self.M
        N = self. N
        return sum(term(k, x) for k in range(M, N+1))
    
def test_Sum():
    term = lambda k, x: (-x)**k
    S = Sum(term, M=0, N=3)
    x = 0.5
    success_1 = abs(S(x) - 0.625) < 1e-12
    success_2 = abs(S.term(3, x) - term(3, x)) < 1e-12
    success = success_1 and success_2
    msg = 'Error in class Sum'
    assert success, msg
    
from math import factorial, pi
import numpy as np
import matplotlib.pyplot as plt
term = lambda k, x: (-1)**k*x**(2*k+1) / factorial(2*k+1)
N = 10
x = np.linspace(-10, 10, 200)
S_sin = Sum(term, 0, N)
plt.figure
plt.plot(x,S_sin(x))
plt.xlabel('x')
plt.ylabel('Taylor approximation of sin(x)')
plt.show()