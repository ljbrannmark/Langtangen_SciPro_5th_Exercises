# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 23:23:08 2020

@author: lars-johan.brannmark
"""

import numpy as np
from math import exp, sin, cos

x = np.array([0, 2],'float')
t = np.array([1, 1.5],'float')

#Compute the expression y = cos(sin(x)) + exp(1/t), 
#as if done using a calculator
u = np.zeros_like(x)
r = np.zeros_like(x)
y = np.zeros_like(x)
for i in range(len(x)):
    #Compute first term
    u[i] = sin(x[i])
    u[i] = cos(u[i])
    #Compute second term
    r[i] = 1/t[i]
    r[i] = exp(r[i])
    #Compute sum
    y[i] = u[i] + r[i]

#Check result using NumPy
y_check = np.cos(np.sin(x)) + np.exp(1/t)

print y
print y_check