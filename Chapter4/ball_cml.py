# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:18:07 2019

@author: lars-johan.brannmark
"""
import sys

v0 = float(sys.argv[1])
t = float(sys.argv[2])
g = 9.81;
y = v0*t - 0.5*g*t**2
print y
