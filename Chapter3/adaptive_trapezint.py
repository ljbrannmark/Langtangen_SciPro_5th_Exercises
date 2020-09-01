# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 23:12:14 2019

@author: larsjohan
"""
from math import sqrt, pi, sin, cos, ceil

def trapezint(f, a, b, n):
    h = float(b-a)/n
    s=0.0
    for i in range(1,n):
        xi = a + i*h
        s += f(xi)
    I = 0.5*h*(f(a)+f(b)) + h*s
    return I

def diff2(f, x, h=1E-6):
    return (f(x+h)-2*f(x)+f(x-h))/(h**2)

def adaptive_trapezint(f, a, b, eps=1E-5):
    n0=100
    h0=float(b-a)/n0
    d2f=[]
    for i in range(n0):
        x=a+i*h0
        d2f.append( abs( diff2(f, x) ) )
        
    h = sqrt(12*eps) / sqrt( (b-a)*max(d2f) )
    n = int( ceil(float(b-a) / h) )
    I = trapezint(f, a, b, n)
    return I, n

I0_exact = 0
I1_exact = 2
I2_exact = 1

eps=1E-5
I0, n0 = adaptive_trapezint(cos, 0, pi, eps)
I1, n1 = adaptive_trapezint(sin, 0, pi, eps)
I2, n2 = adaptive_trapezint(sin, 0, pi/2, eps)

e0 = I0_exact - I0
e1 = I1_exact - I1
e2 = I2_exact - I2

print 'Integral 1, error: %.4e, n=%d' %(e0,n0)
print 'Integral 2, error: %.4e, n=%d' %(e1,n1)
print 'Integral 3, error: %.4e, n=%d' %(e2,n2)