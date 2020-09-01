# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:34:03 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x, t):
    return np.exp(-(x - 3*t)**2)*np.sin(3*np.pi * (x - t))

x = np.linspace(-4, 4, 1000)
t = 0.0
plt.figure()
plt.plot(x, f(x, t))
plt.show()