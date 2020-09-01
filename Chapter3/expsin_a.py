# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:44:36 2019

@author: larsjohan
"""

from math import *

def h(t,a=1.0):
    return exp(-a*t)*sin(pi*t)

print 'h(0,a=10)=%.10e' %h(0,a=10)
print 'h(1,a=10)=%.10e' %h(1,a=10)