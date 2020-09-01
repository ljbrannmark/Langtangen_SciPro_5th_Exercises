# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 22:22:51 2019

@author: larsjohan
"""
from math import *

def g(t):
    return exp(-t)*sin(pi*t)

print 'g(0)=%.10e' %g(0)
print 'g(1)=%.10e' %g(1)