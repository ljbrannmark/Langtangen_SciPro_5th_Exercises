# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:49:30 2020

@author: lars-johan.brannmark
"""

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
    
class Parabola0(Line):
    pass

c0, c1 = 1, 2
l = Line(c0, c1)
p0 = Parabola0(c0, c1)

if dir(l) == dir(p0):
    print 'Line object l and Parabola0 object p0 have same content.'
    print '\nl.__dict__ = %s'%str(l.__dict__)
    print '\np0.__dict__ = %s'%str(p0.__dict__)
    print '\ndir(l) = %s' %str(dir(l))
    print '\ndir(p0) = %s' %str(dir(p0))

