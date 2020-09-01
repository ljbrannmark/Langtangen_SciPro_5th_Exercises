# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 00:39:38 2018

@author: larsjohan
"""
from math import pi,log

M = 67.0 # g
rho = 1.038 # g cm^-3
c = 3.7 # J g^-1 K^-1 
K = 5.4e-3 # W cm^-1 K^-1
T_w = 100.0 # degrees Celsius
T_y = 70.0 # Degrees Celsius

# Case 1, Egg from fridge:
T_o = 4 # degrees Celsius
t_4 = ( M**(2.0/3.0)*c*rho**(1.0/3.0) ) / ( K * pi**2 * (4.0*pi/3)**(2.0/3.0) ) \
* log( 0.76*(T_o-T_w)/(T_y-T_w) )

# Case 2, Egg from room temperature:
T_o = 20 # degrees Celsius
t_20 = ( M**(2.0/3.0)*c*rho**(1.0/3.0) ) / ( K * pi**2 * (4.0*pi/3)**(2.0/3.0) ) \
* log( 0.76*(T_o-T_w)/(T_y-T_w) )

print "t_4 = %.2f s ; t_20 = %.2f s" %(t_4,t_20)