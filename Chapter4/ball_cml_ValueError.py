# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:19:48 2019

@author: lars-johan.brannmark
"""

import sys

v0 = float(sys.argv[1])
t = float(sys.argv[2])
g = 9.81;

if not (0 <= t <= 2*v0/g):
    raise ValueError('The value of t must be in the interval 0 <= t <= %f.' %(2*v0/g) )
    
y = v0*t - 0.5*g*t**2
print y