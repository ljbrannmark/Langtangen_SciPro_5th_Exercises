# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 00:21:18 2020

@author: lars-johan.brannmark
"""

import numpy as np

def simulate_binomial(p, n, x):
    N = 1000000
    r = np.random.random(size=(n, N))
    M = np.sum(np.sum(r <= p, axis=0) == x)
    B_est = M/float(N)
    B = np.math.factorial(n)/float(np.math.factorial(x) \
            *np.math.factorial(n-x))*p**x*(1-p)**(n-x)
    error = B_est - B
    return B_est, error

print 'Probability of 2 heads, flipping coin 5 times: %g'%(simulate_binomial(0.5, 5, 2)[0])
print 'Probability of 4 ones in a row, throwing a die: %g'%(simulate_binomial(1/6.0, 4, 4)[0])
print 'Probability of breaking a ski in five competitions: %g'%(1-simulate_binomial(1/120.0, 5, 0)[0])