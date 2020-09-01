# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 02:47:58 2018

@author: larsjohan
"""
from numpy import sqrt, exp, pi

m = 0.0
s = 2.0
x = 1.0

f_x = 1.0 / ( sqrt(2*pi)*s ) * exp( -1.0/2 * ( (x-m)/s )**2 )

print "f(x) = %g" %f_x