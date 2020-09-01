# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 15:29:51 2019

@author: lars-johan.brannmark
"""

import sys

v0 = float(sys.argv[1])      # Velocity in km/h
mu = float(sys.argv[2])      # Friction coefficient (dimensionless)
g = 9.81                     # Gravity constant

d = 0.5 * (v0/3.6)**2 / (mu*g)

print 'With v0=%.1f km/h, mu=%.2f, the braking distance is d = %.1f m.' %(v0,mu,d)