# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 01:57:42 2018

@author: larsjohan
"""

#Task a)
from math import sin, cos
x=pi/4
val_1=sin(x)**2 + cos(x)**2
print "Task a) sin^2(x) + cos^2(x) = %g" % val_1

#Task b)
v0=3.0
t=1.0
a=2.0
s=v0*t + 0.5*a*t**2
print "Task b) s = %g" % s

#Task c)
a=3.3; b=5.3
a2=a**2
b2=b**2

eq1_sum = a2 + 2*a*b + b2
eq2_sum = a2 - 2*a*b + b2

eq1_pow = (a + b)**2
eq2_pow = (a - b)**2

print "Task c)"
print "First equation: %g = %g" % (eq1_sum, eq1_pow)
print "Second equation: %g = %g" % (eq2_sum, eq2_pow)