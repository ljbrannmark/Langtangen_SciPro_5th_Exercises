# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 22:27:52 2020

@author: lars-johan.brannmark
"""

class Line(object):
    def __init__(self, c0, c1):
        self.c0 = c0
        self.c1 = c1

    def __call__(self, x):
        print 'In function: Line.__call__: self.c0 + self.c1*x'
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
        print 'In function: Parabola.__call__: Line.__call__(self.x) + self.c2*x**2'
        return Line.__call__(self, x) + self.c2*x**2
    
class Cubic(Parabola):
    def __init__(self, c0, c1, c2, c3):
        Parabola.__init__(self, c0, c1, c2)
        self.c3 = c3
        
    def __call__(self, x):
        print 'In function: Cubic.__call__: Parabola.__call__(self.x) + self.c3*x**3'
        return Parabola.__call__(self, x) + self.c3*x**3
    
class Poly4(Cubic):
    def __init__(self, c0, c1, c2, c3, c4):
        Cubic.__init__(self, c0, c1, c2, c3)
        self.c4 = c4
        
    def __call__(self, x):
        print 'In function: Poly4.__call__: Cubic.__call__(self.x) + self.c4*x**4'
        return Cubic.__call__(self, x) + self.c4*x**4
    
x = 4.0
c = Cubic(1.0, 1.5, 2.0, 1.5)
p = Poly4(1.0, 1.5, 2.0, 1.5, 1.5)

print 'c(%g)=%g'%(x, c(x))
print
print 'p(%g)=%g'%(x, p(x))


    