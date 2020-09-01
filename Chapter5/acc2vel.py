# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 23:12:52 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

dt = float(raw_input('dt: '))

a = np.loadtxt('acc.dat')
t = np.linspace(0,dt*(len(a)-1),len(a))

#------------------------------------------------------------------------------
# Compute v(t_k)
v = np.zeros_like(a)
for k in range(1,len(a)):
    v[k] = v[k-1] + dt*0.5*(a[k-1]+a[k])

#------------------------------------------------------------------------------
# Plot acceleration data
plt.figure()
plt.plot(t,v)
plt.xlabel('$t_k$ $[s]$')
plt.ylabel('v [$m/s$]')
plt.title('Velocity versus time')
plt.show()
