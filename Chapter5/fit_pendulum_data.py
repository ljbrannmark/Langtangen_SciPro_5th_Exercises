# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 21:48:53 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('pendulum.dat',skiprows=1)

L = data[:,0]
T = data[:,1]

#------------------------------------------------------------------------------
# Plot the pendulum data in L, T
plt.figure()
plt.plot(L,T,'bo')
plt.xlabel('L $[m]$')
plt.ylabel('T [$s$]')
plt.title('Pendulum data')
plt.show()

#------------------------------------------------------------------------------
# Plot the pendulum data and fitted polynomials with degrees specified in deg
deg = [1, 2, 3]
L_eval = np.linspace(min(L),max(L),10*len(L))
plt.figure()
plt.plot(L, T, 'bo', label='Data points')
plt.xlabel('L $[m]$')
plt.ylabel('T [$s$]')
plt.title('Pendulum data')
for i in range(len(deg)):
    coeff = np.polyfit(L, T, deg[i])
    p = np.poly1d(coeff)
    plt.plot(L_eval, p(L_eval), label='Polynomial fit, degree %d'%deg[i])
plt.legend()
plt.show()






