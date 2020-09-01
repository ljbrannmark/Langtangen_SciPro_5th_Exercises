# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 00:05:57 2020

@author: lars-johan.brannmark
"""
import numpy as np
import matplotlib.pyplot as plt

def trapezoidal(f, a, x, n):
    h = (x-a)/float(n)
    I = 0.5*f(a)
    for i in range(1, n):
        I += f(a + i*h)
    I += 0.5*f(x)
    I *= h
    return I

class Integral(object):
    def __init__(self, f, a, n=100):
        self.f, self.a, self.n = f, a, n

    def __call__(self, x):
        f, a, n = self.f, self.a, self.n
        if isinstance(x, np.ndarray):
            F = np.zeros_like(x)
            F[0] = trapezoidal(f, a, x[0], n)
            for k in range(1,len(x)):
                n_k = int(np.ceil(n*(x[k]-x[k-1])/(x[-1]-a)))
                F[k] = F[k-1] + trapezoidal(f, x[k-1], x[k], n_k)
        else:
            F = trapezoidal(f, a, x, n) 
        return F
    
def test_Integral():
    a = 1
    xm = a + 5
    I = Integral(lambda x: x, a, 1000)
    x = np.linspace(a, xm, 100)
    success = np.allclose(I(x), (x**2-a**2)/2.0, rtol=1e-12, atol=1e-12)
    msg = "Error in class Integral"
    assert success, msg

test_Integral()
