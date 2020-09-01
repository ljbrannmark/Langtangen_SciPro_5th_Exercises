# -*- coding: utf-8 -*-
"""
Created on Fri Mar 01 16:46:18 2019

@author: larsjohan
"""

n=10

v0=20.0
g=9.81

a=0.0
b=2*v0/g

h=float(b-a)/n

T=[a + i*h for i in range(n+1)]
Y=[v0*t - 1.0/2*g*t**2 for t in T ]

for t,y in zip(T,Y):
    print '%10.4g %10.4g' %(t,y)
    
    
    
    