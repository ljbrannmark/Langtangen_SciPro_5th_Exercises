# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:02:32 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def my_rand(N, a=8121, c=28411, m=134456, seed=1):
    x = np.zeros(shape=N, dtype=float)
    for n in range(1,N-1):
        x[n] = (a*x[n-1] + c) % m
    y = x / float(m)
    return y
        
N = 100000
x = my_rand(N)
plt.hist(x, bins=20, histtype='step')