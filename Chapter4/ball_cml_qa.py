# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:56:32 2019

@author: lars-johan.brannmark
"""

import sys

try:
    v0 = float(sys.argv[1])
except IndexError:
    v0 = float(raw_input('v0 not provided at command line. v0=? '))

try:
    t = float(sys.argv[2])
except IndexError:
    t = float(raw_input('t not provided at command line. t=? '))
    
g = 9.81;
y = v0*t - 0.5*g*t**2
print y
