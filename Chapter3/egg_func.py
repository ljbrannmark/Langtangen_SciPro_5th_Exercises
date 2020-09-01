# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 23:14:14 2019

@author: larsjohan
"""
from math import pi,log

def egg(M, To=20, Ty=70):
    rho = 1.038 # g cm^-3
    K = 5.4e-3 # W cm^-1 K^-1
    c = 3.7 # J g^-1 K^-1 
    Tw = 100.0 # degrees Celsius
    
    t = ( M**(2.0/3.0)*c*rho**(1.0/3.0) ) / ( K * pi**2 * (4.0*pi/3.0)**(2.0/3.0) ) \
    * log( 0.76*(To-Tw)/(Ty-Tw) )
    return t

t_soft_small_fridge = egg(47.0, 4.0, 63.0)
t_soft_small_room = egg(47.0, 25.0, 63.0)

t_soft_large_fridge = egg(67.0, 4.0, 63.0)
t_soft_large_room = egg(67.0, 25.0, 63.0)

t_hard_small_fridge = egg(47.0, 4.0, 70.0)
t_hard_small_room = egg(47.0, 25.0, 70.0)

t_hard_large_fridge = egg(67.0, 4.0, 70.0)
t_hard_large_room = egg(67.0, 25.0, 70.0)
