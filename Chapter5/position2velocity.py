# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 21:23:59 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

s = float(np.loadtxt('pos.dat', max_rows=1))
xy_data = np.loadtxt('pos.dat', skiprows=1)

x_data = xy_data[:,0]
y_data = xy_data[:,1]

plt.figure()
plt.plot(x_data,y_data)
plt.xlabel('x [m]')
plt.ylabel('y [m]')

t = s*np.array(range(len(x_data)-1))

v_x = np.diff(x_data,1) / s
v_y = np.diff(y_data,1) / s

plt.figure()
plt.plot(t,v_x)
plt.xlabel('$t [s]$')
plt.ylabel('$v_x(t) [m/s]$')

plt.figure()
plt.plot(t,v_y)
plt.xlabel('$t [s]$')
plt.ylabel('$v_y(t) [m/s]$')