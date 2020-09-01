# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 23:06:11 2020

@author: lars-johan.brannmark
"""

import sys
import numpy as np
import matplotlib.pyplot as plt

y = lambda t, v0, g: v0*t - 1.0/2 * g*t**2

g = 9.81
v0_array = np.array([float(number) for number in sys.argv[1:]])

tmin = 0
tmax = max(2.0*v0_array/g)
ymin = []
ymax = []

plt.figure(1)
for v0 in v0_array:
    t = np.linspace(tmin, 2*v0/g, 100)
    yv = y(t, v0, g)
    plt.plot(t, yv)
    ymin.append(min(yv))
    ymax.append(max(yv))

plt.axis([tmin, tmax, min(ymin), 1.10*max(ymax)])
plt.xlabel('time (s)')
plt.ylabel('height (m)')

plt.show()