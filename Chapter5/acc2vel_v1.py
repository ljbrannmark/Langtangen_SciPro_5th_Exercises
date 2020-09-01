# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 22:34:00 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

dt = float(raw_input('dt: '))
k = int(raw_input('k: '))

a = np.loadtxt('acc.dat')
t = np.linspace(0,dt*(len(a)-1),len(a))

#------------------------------------------------------------------------------
# Plot acceleration data

plt.figure()
plt.plot(t,a)
plt.xlabel('$t_k$ $[s]$')
plt.ylabel('a [$m/s^2$]')
plt.title('Acceleration versus time')
plt.show()

#------------------------------------------------------------------------------
# Compute v(t_k)

v = dt*(0.5*a[0] + 0.5*a[k] + np.sum(a[1:k-1]) )

print "\ndt=%.2f, k=%d, t_k=%.1f: v(t_k)=%.3f m/s"%(dt, k, t[k], v)