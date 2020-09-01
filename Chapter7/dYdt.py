# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:29:47 2020

@author: lars-johan.brannmark
"""

from Derivative import Derivative
from Y import Y

v0 = 10
y = Y(v0)
dydt = Derivative(y)

t = 0
print 't=0'
print 'dydt(t)=%g' %dydt(t)
print 'v0-gt=%g' %(v0 - y.g*t)
print

t = 0.5*v0/y.g
print 't=1/2 * v0/g'
print 'dydt(t)=%g' %dydt(t)
print 'v0-gt=%g' %(v0 - y.g*t)
print

t = v0/y.g
print 't=v0/g'
print 'dydt(t)=%g' %dydt(t)
print 'v0-gt=%g' %(v0 - y.g*t)
print