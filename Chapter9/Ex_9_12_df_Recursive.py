# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 23:12:15 2020

@author: lars-johan.brannmark
"""
class Diff(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)
        
class Central2(Diff):
    def __call__(self, x):
        f, h = self.f, self.h
        return (f(x+h) - f(x-h))/(2*h)


ddf = Central2(Central2(lambda x: x**4))
ddf_exact = lambda x: 12.0*x**2

print 'Central2(Central2(lambda x: x**4))(2.0) = %f'%ddf(2.0)
print '12.0*2.0**2 = %f'%ddf_exact(2.0)
