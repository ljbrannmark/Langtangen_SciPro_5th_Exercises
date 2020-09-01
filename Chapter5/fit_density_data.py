# -*- coding: utf-8 -*-
"""
Created on Mon Jan 27 21:12:06 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

#------------------------------------------------------------------------------
def fit(x,y,deg):
    plt.figure()
    plt.plot(x, y, 'ro', label='data')
    x_eval = np.linspace(min(x),max(x),10*len(x))
    for i in range(len(deg)):
        coeff = np.polyfit(x, y, deg[i])
        p = np.poly1d(coeff)
        plt.plot(x_eval, p(x_eval), label='fitted polynomial of degree %d'%deg[i])
    plt.xlabel('temp $[^\circ C]$')
    plt.ylabel('density [$kg/m^3$]')
    plt.legend()
    plt.show()
#------------------------------------------------------------------------------
data = np.loadtxt('density_water.dat')
fit(data[:,0], data[:,1], [1, 2])

    
    
    
