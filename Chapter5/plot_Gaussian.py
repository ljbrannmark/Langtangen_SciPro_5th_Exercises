# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 00:02:39 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def h(x):
    return 1.0/np.sqrt(2*np.pi) * np.exp( -x**2 / 2.0 )

x = np.linspace(-4,4,41)
y = h(x)

plt.plot(x,y)
plt.xlabel('x')
plt.ylabel('y')