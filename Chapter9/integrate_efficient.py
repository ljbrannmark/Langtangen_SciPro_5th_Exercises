# -*- coding: utf-8 -*-
"""
Created on Fri Sep 25 21:50:12 2020

@author: lars-johan.brannmark
"""

# The instructions in the exercise 9.16 are quite vague:
# Is x an array? is self.a = x[0], or just self.a <= x[0]? 
#Is self.a <= x[k] <= self.b ? Or should a and x be chosen freely in
#the computation of F(x)?


import numpy as np
import math

class Integrator(object):
    def __init__(self, a, b, n):
        self.a, self.b, self.n = a, b, n
        self.points, self.weights = self.construct_method()

    def construct_method(self):
        raise NotImplementedError('no rule in class %s' %
                                  self.__class__.__name__)

    def integrate(self, f):
        s = 0.0
        for i in range(len(self.weights)):
            s += self.weights[i]*f(self.points[i])
        return s

    def vectorized_integrate(self, f):
        return np.dot(self.weights, f(self.points))
    
    def F(self, f, a, x):
        #Method for computing F(x) = integral of f(x) from a to x, where
        #f and a can be set freely, and x may be an array of values:
        # a <= x[0] < x[1] < ... < x[m].
        F = np.zeros_like(x)
        n = self.n
        #How many points between a and x[0] ? 
        n_0 = int(np.ceil(n*(x[0]-a)/(x[-1]-a)))
        if n_0 == 0:
            F[0] = 0
        else:
            #Create a new integral object i, to integrate from a to x[0]
            i = self.__class__(a, x[0], n_0)
            F[0] = i.integrate(f)
        for k in range(1,len(x)):
            n_k = int(np.ceil(n*(x[k]-x[k-1])/(x[-1]-a)))
            #Create a new integral object i, to integrate from x[k-1] to x[k]
            i = self.__class__(x[k-1], x[k], n_k)
            F[k] = F[k-1] + i.integrate(f)
        return F


class Midpoint(Integrator):
    def construct_method(self):
        a, b, n = self.a, self.b, self.n  # quick forms
        h = (b-a)/float(n)
        x = np.linspace(a + 0.5*h, b - 0.5*h, n)
        w = np.zeros(len(x)) + h
        return x, w

class Trapezoidal(Integrator):
    def construct_method(self):
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)
        w = np.zeros(len(x)) + h
        w[0] /= 2
        w[-1] /= 2
        return x, w

class Simpson(Integrator):
    def construct_method(self):
        if self.n % 2 != 1:
            print 'n=%d must be odd, 1 is added' % self.n
            self.n += 1
        x = np.linspace(self.a, self.b, self.n)
        h = (self.b - self.a)/float(self.n - 1)*2
        w = np.zeros(len(x))
        w[0:self.n:2] = h*1.0/3
        w[1:self.n-1:2] = h*2.0/3
        w[0] /= 2
        w[-1] /= 2
        return x, w

class GaussLegendre2(Integrator):
    def construct_method(self):
        if self.n % 2 != 0:
            print 'n=%d must be even, 1 is subtracted' % self.n
            self.n -= 1
        nintervals = int(self.n/2.0)
        h = (self.b - self.a)/float(nintervals)
        x = np.zeros(self.n)
        sqrt3 = 1.0/math.sqrt(3)
	for i in range(nintervals):
            x[2*i]   = self.a + (i+0.5)*h - 0.5*sqrt3*h
            x[2*i+1] = self.a + (i+0.5)*h + 0.5*sqrt3*h
        w = np.zeros(len(x)) + h/2.0
        return x, w

class GaussLegendre2_vec(Integrator):
    def construct_method(self):
        if self.n % 2 != 0:
            print 'n=%d must be even, 1 is added' % self.n
            self.n += 1
        nintervals = int(self.n/2.0)
        h = (self.b - self.a)/float(nintervals)
        x = np.zeros(self.n)
        sqrt3 = 1.0/math.sqrt(3)
        m = np.linspace(0.5*h, (nintervals-1+0.5)*h, nintervals)
        x[0:self.n-1:2] = m + self.a - 0.5*sqrt3*h
        x[1:self.n:2]   = m + self.a + 0.5*sqrt3*h
        w = np.zeros(len(x)) + h/2.0
        return x, w


def test_F():
    """Check that linear functions are integrated exactly."""
    def f(x):
        return 2*x - 3

    def F(x):
        """Integral of f."""
        return x**2 - 3*x

    a = 1; b = 6; n = 1001    # test data
    x = np.linspace(a, a+10, 100)
    I_exact = F(x) - F(a)
    tol = 1E-13

    methods = [Midpoint, Trapezoidal, Simpson, GaussLegendre2,
               GaussLegendre2_vec]
    
    for method in methods:
        integrator = method(a, b, n)

        I = integrator.F(f, a, x)
        assert (abs(I_exact - I) < tol).all()

if __name__ == '__main__':
    test_F()
