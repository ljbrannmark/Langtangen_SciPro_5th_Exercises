# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 22:20:58 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

A = 1
T = 2*np.pi
h = T/40.0
n = 200
i = np.arange(n+1)

t = i*h
etabar = A*np.sin(2*np.pi/T*t)

plt.figure()
plt.plot(t, etabar, label='$\\bar{\eta}$')
plt.xlabel('t')

sigma_E = 0.04*A
E = np.random.normal(loc=0.0, scale=sigma_E, size=etabar.size)

eta = etabar + E

plt.plot(t, eta, 'bo', fillstyle='none', label='$\eta$')
plt.legend()
plt.show()

j = i[1:-1]
detabar = (etabar[j+1]-etabar[j-1])/(2*h)

plt.figure()
plt.plot(t[1:-1], detabar, label='$\\frac{d}{dt}\\bar{\eta}$')
plt.xlabel('t')
plt.legend()
plt.show()

dE = (E[j+1]-E[j-1])/(2*h) 

m_dE = dE.mean()
sigma_dE = dE.std()

plt.figure()
plt.plot(t[1:-1], detabar, label='$\\frac{d}{dt}\\bar{\eta}$')
plt.plot(t[1:-1], detabar+dE, label='$\\frac{d}{dt}\\bar{\eta}$+$\\frac{d}{dt}E$')
plt.xlabel('t')
plt.legend()
plt.show()

d2etabar = (etabar[j+1]-2*etabar[j]+etabar[j-1])/(h**2)
d2E = (E[j+1]-2*E[j]+E[j-1])/(h**2)

m_d2E = d2E.mean()
sigma_d2E = d2E.std()

plt.figure()
plt.plot(t[1:-1], d2etabar, label='$\\frac{d^2}{dt^2}\\bar{\eta}$')
plt.plot(t[1:-1], d2etabar+d2E, label='$\\frac{d^2}{dt^2}\\bar{\eta}$+$\\frac{d^2}{dt^2}E$')
plt.xlabel('t')
plt.legend()
plt.show()

#We have, theoretically (holds only approximately for the data):
# sigma_dE = sigma_E*np.sqrt(1+1)/(2*h)
# sigma_d2E = sigma_E*np.sqrt(1+4+1)/h**2
