# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:13:25 2019

@author: lars-johan.brannmark
"""

t = float(raw_input('t=? '))
v0 = float(raw_input('v0=? '))
g = 9.81;
y = v0*t - 0.5*g*t**2
print y
