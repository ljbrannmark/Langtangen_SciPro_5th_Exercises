# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 22:39:08 2020

@author: lars-johan.brannmark
"""
# Exercise 8.30 a)
#
# Compute integral of f(x) betwen x=0 and x=1, where
#
# f(x) = 1 / (1-x**2)**(1/2)
#
# The primitive function of f(x) is arcsin(x), so integral becomes
#
# arcsin(1)-arcsin(0) = pi/2 - 0 = pi/2
#
# Monte Carlo approach:
#
# Compute E[f(x)] = 1/(N+1)*sum(f(xi)), with xi uniformly distributed
# between 0 and 1.  Sum converges to pi/2. So 2*sum is an approximation of pi.

# Exercise 8.30 b)
import numpy as np
import matplotlib.pyplot as plt
from math import pi

Nmax = 10**6
f = lambda x: (1-x**2)**(-0.5)

#Generate x_0, x_1, ..., x_N
x = np.random.random(Nmax+1) 
#Create vector of N+1, for N=0, ..., Nmax
Np1 = np.arange(0, Nmax+1, dtype=float) + 1 

S = 2/Np1*np.cumsum(f(x))

plt.figure;
plt.plot(Np1-1, S, label='$S_N$')
plt.plot([0, Nmax], [pi, pi], label='$\pi$')
plt.xlabel('$N$')
plt.ylabel('$S_N$')
plt.legend()
plt.show()