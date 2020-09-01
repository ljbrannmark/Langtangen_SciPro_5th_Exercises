# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:59:55 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
from math import factorial

def S(x, n):
    x = np.asarray(x)
    s = np.zeros_like(x)
    for j in range(n+1):
        s += (-1)**j * x**(2.0*j + 1) / float(factorial(2*j + 1))
    return s

x = np.linspace(0, 4*np.pi, 1000)
plt.figure()
plt.plot(x, np.sin(x))
for n in [1, 2, 3, 6, 12]:
    plt.plot(x, S(x, n))
plt.axis([0, 4*np.pi, -3, 3])
plt.xlabel('x')
plt.ylabel('Approximations of sin(x)')
plt.show()    
