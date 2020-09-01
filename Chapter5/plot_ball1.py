# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 22:57:18 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

v0 = 10
g = 9.81
t = np.linspace(0, 2*v0/g, 100)

y = v0*t - 1.0/2 * g*t**2 

plt.figure(1)
plt.plot(t, y)
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.show()