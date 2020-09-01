# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:34:25 2020

@author: lars-johan.brannmark
"""

import numpy as np
from math import sqrt, exp, pi

def h(x):
    return 1.0/sqrt(2*pi) * exp(-1.0/2 * x**2)

n = 41
x0 = -4.0
x1 = 4.0
dx = float(x1-x0)/(n-1)

x = np.zeros(n)
y = np.zeros(n)
for i in range(n):
    x[i] = x0 + i*dx
    y[i] = h(x[i])
    
