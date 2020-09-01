# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 23:05:29 2020

@author: lars-johan.brannmark
"""
import sys
import matplotlib.pyplot as plt
import numpy as np

g = 9.81

f = lambda x: x*np.tan(theta) - 1.0/(2.0*v0**2) * g*x**2 / (np.cos(theta)**2) + y0

y0 = float(sys.argv[1])
theta = float(sys.argv[2])/180*np.pi
v0 = float(sys.argv[3])

#Compute the root of f(x)=0
x0 = v0*np.cos(theta)/g * ( v0*np.sin(theta) + np.sqrt(2*g*y0 + v0**2*np.sin(theta)**2) )

x = np.linspace(0,x0,100)
y = f(x)

plt.figure(1)
plt.plot(x,y)
plt.axis('equal')