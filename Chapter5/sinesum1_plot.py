# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 00:01:09 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def S(t,n,T=2*np.pi):
    s = np.zeros_like(t)
    for i in range(1,n+1):
        s += 1.0/(2*i - 1) * np.sin( 2*(2*i - 1)*np.pi*t / T )
    s = 4.0/np.pi * s
    return s

def f(t, T = 2*np.pi):
    y = np.zeros_like(t)
    cond1 = np.logical_and(0 < t, t < T/2.0 )
    cond2 = t == T/2.0
    cond3 = np.logical_and(T/2.0 < t, t < T )
    y[cond1] = 1.0
    y[cond2] = 0.0
    y[cond3] = -1.0
    return y

T = 2*np.pi
t = np.linspace(0, T, 1000)

plt.figure()
plt.plot(t,S(t,1),label='n=1')
plt.plot(t,S(t,3),label='n=3')
plt.plot(t,S(t,20),label='n=20')
plt.plot(t,S(t,200),label='n=200')
plt.plot(t,f(t),label='Exact')
plt.xlabel('t')
plt.ylabel('S(t;n)')
plt.legend()
plt.show()