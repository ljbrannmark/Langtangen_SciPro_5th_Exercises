# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 23:06:29 2020

@author: lars-johan.brannmark
"""
from math import sin

class Line(object):
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        return self.c0 + self.c1*x

    def table(self, L, R, n):
        """Return a table with n points for L <= x <= R."""
        s = ''
        import numpy as np
        for x in np.linspace(L, R, n):
            y = self(x)
            s += '%12g %12g\n' % (x, y)
        return s

class Parabola(Line):
    def __init__(self, c0, c1, c2):
        Line.__init__(self, c0, c1)  # let Line store c0 and c1
        self.c2 = c2

    def __call__(self, x):
        return Line.__call__(self, x) + self.c2*x**2
    
class F(Parabola):
    #Implements f(x) = A*sin(w*x) + a*x**2 + b*x + c
    def __init__(self, A, w, a, b, c):
        Parabola.__init__(self, c, b, a)
        self.A = A
        self.w = w
    
    def __call__(self, x):
        return self.A*sin(self.w*x) + Parabola.__call__(self, x)
    
    def table(self, L, R, n):
        s = '%12s %12s\n%s\n%s' %('x', 'f(x)', '-'*25, super(Parabola, self).table(L, R, n))
        return s
    
A, w, a, b, c = 4.0, 2.0, 5.0, 3.0, 1.0
x = 4.5
f = F(A, w, a, b, c)

print 'x = %g'%x
print 'f(x) = %g'%f(x)
print 'Check: %g*sin(%g*x) + %g*x**2 + %g*x + %g = %g'%(A, w, a, b, c, A*sin(w*x) + a*x**2 + b*x + c)
    
print '\nTable:'
print f.table(0, 5, 11)    
    