# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 21:41:23 2020

@author: lars-johan.brannmark
"""
import numpy as np
import matplotlib.pyplot as plt

R = 10
N = 5000
T = 180
dt = T/float(N)
t = np.arange(0,N+1)*dt

mu = 0.01
sigma = 0.03
x0 = np.array([100]*R)

def stock_sim(mu, sigma, x0, N, T):
    R = len(x0)
    dt = T/float(N)
    X = np.zeros((N+1,R), dtype=float)
    X[0, :] = x0
    for n in range(1,N+1):
        r = np.random.normal(loc=0.0, scale=1.0, size=R)
        X[n,:] = X[n-1,:]*(1 + dt*mu + sigma*np.sqrt(dt)*r)
    return X

X = stock_sim(mu, sigma, x0, N, T)

plt.figure()
plt.plot(t,X)
plt.xlabel('time [days]')
plt.ylabel('stock price')
