# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:02:21 2020

@author: lars-johan.brannmark
"""

import numpy as np
x = np.linspace(0, 2, 20)
y = x*(2 - x)
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()

plt.figure()
y = np.cos(18*np.pi*x)
plt.plot(x, y)
plt.show()

x = np.linspace(0, 2, 1000)
y = np.cos(18*np.pi*x)
plt.plot(x, y)
plt.show()