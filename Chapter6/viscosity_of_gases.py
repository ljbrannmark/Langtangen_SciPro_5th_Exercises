# -*- coding: utf-8 -*-
"""
Created on Fri May  8 22:14:14 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

filename = 'viscosity_of_gases.dat'
with open(filename,'r') as infile:
    lines = infile.readlines()
    ind = lines.index('#   gas           C     T_0     mu_0\n') + 1
    mu_data = {' '.join(line.split()[0:-3]): 
        {'C': float(line.split()[-3]),
         'T_0': float(line.split()[-2]),
         'mu_0': float(line.split()[-1])} for line in lines[ind:ind+8]}
    
def mu(T, gas, mu_data):
    mu_0 = mu_data[gas]['mu_0']
    T_0 = mu_data[gas]['T_0']
    C = mu_data[gas]['C']
    return mu_0 * (T_0 - C) / (T + C) * (T/T_0)**1.5

T = np.linspace(223.0, 373.0, num=100)
plt.figure(1)
plt.plot(T, mu(T, 'air', mu_data), label='air')
plt.plot(T, mu(T, 'carbon dioxide', mu_data), label='carbon dioxide')
plt.plot(T, mu(T, 'hydrogen', mu_data), label='hydrogen')
plt.xlabel('T')
plt.ylabel('$\mu(T)$')
plt.legend()
plt.show()