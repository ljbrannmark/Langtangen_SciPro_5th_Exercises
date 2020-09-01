# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 22:47:09 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

m = float(raw_input('m: '))
v0 = float(raw_input('v0: '))

g = 9.81
t = np.linspace(0, 2*v0/g, 501)

y = v0*t - 0.5*g*t**2
v = v0 - g*t

P = m*g*y
K = 0.5*m*v**2

plt.figure()
plt.plot(t, P, label='P(t)')
plt.plot(t, K, label='K(t)')
plt.plot(t, P+K, label='P+K')
plt.xlabel('Time [s]')
plt.ylabel('Energy [J]')
plt.legend()