# -*- coding: utf-8 -*-
"""
Created on Fri Dec  6 23:20:08 2019

@author: lars-johan.brannmark
"""

def midpoint_integration(f, a, b, n=100):
    h = (b - a)/float(n)
    I = 0
    for i in range(n):
        I += f(a + i*h + 0.5*h)
    return h*I

from math import *
import sys
from scitools.StringFunction import StringFunction

f_formula = sys.argv[1]
a = eval(sys.argv[2])
b = eval(sys.argv[3])
if len(sys.argv) >= 5:
    n = int(sys.argv[4])
else:
    n = 200

f = StringFunction(f_formula)

I = midpoint_integration(f, a, b, n)
print 'Integral of %s on [%g, %g] with n=%d: %g' % \
      (f_formula, a, b, n, I)

