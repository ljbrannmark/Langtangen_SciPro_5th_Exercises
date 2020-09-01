# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:10:39 2020

@author: lars-johan.brannmark
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

y = lambda t, v0, g: v0*t - 1.0/2 * g*t**2

g = 9.81

plt.figure(1)
for number in sys.argv[1:]:
    v0 = float(number)
    t = np.linspace(0, 2*v0/g, 100)
    plt.plot(t, y(t, v0, g))
    
plt.xlabel('time (s)')
plt.ylabel('height (m)')
plt.show()