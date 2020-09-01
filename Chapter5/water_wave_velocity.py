# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 21:19:07 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

g = 9.81    # Acceleration of gravity [m/s^2]
s = 7.9e-2  # Air-water surface tension [N/m]
rho = 1000  # Water density [kg/m^3]
h = 50      # Water depth [m]

c = lambda l: np.sqrt( g*l/(2*np.pi) * ( 1 + s*(4*np.pi**2)/(rho*g*l**2) )*np.tanh( 2*np.pi*h / l ) )

l_small = np.linspace(0.001, 0.1, 1000)
l_large = np.linspace(1.0, 2000, 1000)

plt.figure()
plt.plot(l_small, c(l_small))
plt.xlabel('wavelength $\lambda$ [m]')
plt.ylabel('wave speed c($\lambda$) [m/s]')
plt.show()

plt.figure()
plt.plot(l_large, c(l_large))
plt.xlabel('wavelength $\lambda$ [m]')
plt.ylabel('wave speed c($\lambda$) [m/s]')
plt.show()