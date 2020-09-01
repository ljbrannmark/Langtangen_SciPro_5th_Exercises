# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:29:10 2020

@author: lars-johan.brannmark
"""

import sys
from numpy.lib.scimath import sqrt
from numpy import allclose

class Quadratic(object):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    
    def value(self, x):
        a, b, c = self.a, self.b, self.c
        return a*x**2 + b*x + c
    
    def table(self, L, R, n=10):
        dx = float(R-L)/(n-1)
        print '%15s%15s'%('x', 'f(x)')
        print '-'*30
        for i in range(n):
            x = L+i*dx
            print '%15.7g%15.7g'%(x,self.value(x))
            
    def roots(self):
        a, b, c = self.a, self.b, self.c
        x1 = ( -b + sqrt(b**2-4*a*c) ) / (2.0*a)
        x2 = ( -b - sqrt(b**2-4*a*c) ) / (2.0*a)
        return (x1, x2)
    
def test_Quadratic():
    print 'Testing class Quadratic...'
    q = Quadratic(1, 2, 3)
    q.table(-5, 5, 21)
    rts_exact = (-1 + sqrt(-2), -1 - sqrt(-2))
    rts_computed = q.roots()
    msg = 'Error found in class Quadratic'
    success = allclose(rts_exact, rts_computed, rtol=1e-12, atol=1e-12)
    assert success, msg
    
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test_Quadratic()
        
