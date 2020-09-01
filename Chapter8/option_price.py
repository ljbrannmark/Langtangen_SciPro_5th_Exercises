# -*- coding: utf-8 -*-
"""
Created on Fri Aug 28 22:53:18 2020

@author: lars-johan.brannmark
"""

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

def stock_price(r, sigma, T, s0):
    S = np.zeros(T+1)
    S[0] = s0
    for t in range(T):
        S[t+1] = (1 + r + sigma*np.random.normal())*S[t]
    return S

def stock_average(S):
    return np.mean(S[1:])

def asian_option_price(r, sigma, s0, T, K, N):
    S_av = np.zeros(N)
    for n in range(N):
        S_av[n] = stock_average(stock_price(r, sigma, T, s0))
    p = (1.0 + r)**-T * np.mean(np.maximum(S_av-K, 0))
    print p
    return p

r = 0.0002
sigma = 0.015
s0 = 100
T = 100
K = 102

N_values = np.arange(1000, 200000, 10000)
p = [asian_option_price(r, sigma, s0, T, K, N) for N in N_values]

plt.figure()
plt.plot(N_values, p)
plt.title('Estimated price p as a function of N')
plt.xlabel('N')
plt.ylabel('p')

error = np.abs(p[-1] - p)
def f(x, c):
    return c/np.sqrt(x)
c_est, cov = curve_fit(f, N_values, error)

plt.figure()
plt.plot(N_values, error, label='Error')
plt.plot(N_values, f(N_values, c_est), label='Fitted curve: $c/\sqrt{N}$')
plt.title('Error of estimated price p as a function of N')
plt.xlabel('N')
plt.ylabel('error')
plt.legend()


