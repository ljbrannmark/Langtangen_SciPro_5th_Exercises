# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 02:22:33 2018

@author: larsjohan
"""
from math import pi

g = 9.81 # ms^-2
rho = 1.2 # kg m^-3
a = 0.11 # m
m = 0.43 # kg
C_D = 0.4 # dimensionless
A=pi*a**2 #m^2

#Case 1: Hard kick
V = 120.0*1000/3600 # m/s
F_d = 1.0/2*C_D*rho*A*V**2
F_g = m*g
print "Hard kick (120 km/h): F_d=%.1f N, F_g = %.1f N, F_d/F_g = %.1f" %(F_d,F_g,F_d/F_g)

#Case 2: Soft kick
V = 30.0*1000/3600 # m/s
F_d = 1.0/2*C_D*rho*A*V**2
F_g = m*g
print "Soft kick (30 km/h): F_d=%.1f N, F_g = %.1f N, F_d/F_g = %.1f" %(F_d,F_g,F_d/F_g)
