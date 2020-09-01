# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 23:24:28 2019

@author: larsjohan
"""
from math import exp, pi, sqrt

def gauss(x, m=0, s=1):
    return 1.0/( sqrt(2*pi)*s ) * exp( -0.5*( ( x - m )/s )**2 )

m = 0
s = 1

n = 11
h = float( (m+5*s) - (m-5*s) ) / (n-1)

print "   x   |   f(x)"
print "--------------"
for i in range(n):
    x = m-5*s + i*h
    f = gauss(x)
    print "%6.3f | %6.6f" %(x,f)