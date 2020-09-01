# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 22:32:35 2019

@author: lars-johan.brannmark
"""
from math import factorial, exp
import sys

def Poisson(x, t, nu):
    return ( (nu*t)**x / float(factorial(x)) )* exp(-nu*t)

x = eval(raw_input('x='))
t = eval(raw_input('t='))
nu = eval(raw_input('nu='))

print 'P(x, t, nu)=%.4g\n' %Poisson(x, t, nu)

print 'P(0,1/2,5)=%.4g\n' %Poisson(0,0.5,5)
print 'P(1,2,5)=%.4g\n' %Poisson(1,2,5)
print 'P(2,1/3,5)=%.4g\n' %Poisson(2,1.0/3,5)
print 'P(3,10,1/5)=%.4g\n' %Poisson(3,10,1.0/5)
print 'P(0,1/52,1/5)=%.4g\n' %Poisson(0,1.0/52,1.0/5)
print 'P(0,6,6)=%.4g\n' %Poisson(0,6,6)