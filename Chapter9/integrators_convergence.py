# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 22:14:30 2020

@author: lars-johan.brannmark
"""

import numpy as np
from integrate import Midpoint, Trapezoidal, Simpson

pi  = np.pi
cos = np.cos
sin = np.sin
exp = np.exp
log = np.log

methods = [Midpoint, Trapezoidal, Simpson]
n_values = [2**k + 1 for k in range(2,12)] #[n_0, n_1, ..., n_N]
N = len(n_values)-1

#Dictionaries for storing the errors and estimated constants for each method:
errors = {m.__name__: [0]*(N+1) for m in methods}
rate_constants = {m.__name__: {'r': [0]*N, 'C': [0]*N} for m in methods}

f = lambda x: 2.0 + cos(7.5*pi*x) - x**2 + exp(x)
F = lambda x: 2.0*x + sin(7.5*pi*x)/(7.5*pi) - x**3/3.0 + exp(x)

a = -1.0
b = 1.0

integral_exact = F(b) - F(a)

print '\n%-12s%6s%6s%14s%12s%12s'%('Method', 'i', 'n_i', 'E_i', 'r_i', 'C_i')
for method in methods:
    m = method.__name__
    
    #Compute the errors E_0, ..., E_N
    for i in range(N+1):
        n = n_values[i]
        I = method(a, b, n)
        integral_computed = I.integrate(f)
        errors[m][i] = abs(integral_exact - integral_computed)
    
    #Compute r_i and C_i for i = 1, ..., N-1:
    for i in range(N):
        E_i, E_ip1 = errors[m][i], errors[m][i+1]
        n_i, n_ip1 = n_values[i], n_values[i+1]
        r_i = log(E_i/E_ip1) / log(n_i/float(n_ip1))
        rate_constants[m]['r'][i] = r_i
        rate_constants[m]['C'][i] = E_i*n_values[i]**(-r_i)
    
    #Print the results for current method, for i = 0, ..., N-1
    print '-'*62
    for i in range(N):
        print '%-12s%6d%6d%14.4g%12.4g%12.4g'\
        %(m, i, n_values[i], errors[m][i],\
          rate_constants[m]['r'][i], rate_constants[m]['C'][i])
    i = N
    #Print the results for current method, for i = N
    print '%-12s%6d%6d%14.4g%12s%12s'%(m, i, n_values[i], errors[m][i], 'N/A', 'N/A')
    