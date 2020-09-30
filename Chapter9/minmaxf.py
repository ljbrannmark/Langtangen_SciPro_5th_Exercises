# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 00:07:37 2020

@author: lars-johan.brannmark
"""

import numpy as np

class MinMax(object):
    def __init__(self, f, a, b, n):
        self.f, self.a, self.b, self.n = f, a, b, n
        self.Pmin, self.Pmax, self.Fmin, self.Fmax = self._find_extrema()
    
    def __str__(self):
        s = 'All minima: '
        if len(self.Pmin) > 0:
            for i in self.Pmin[:-1]:
                s += '%.7g, ' %i
            s += '%.7g\n'%self.Pmin[-1]
        s += 'All maxima: '
        if len(self.Pmax) > 0:
            for i in self.Pmax[:-1]:
                s += '%.7g, ' %i
            s += '%.7g\n'%self.Pmax[-1]
        s += 'Global minimum: %.7g\n'%self.get_global_minimum()[0]
        s += 'Global maximum: %.7g'%self.get_global_maximum()[0] 
        return s
    
    def __repr__(self):
        return self.__str__()
        
    def _find_extrema(self):
        f, a, b, n = self.f, self.a, self.b, self.n
        x = np.linspace(a, b, n+1) # x[0], ..., x[n]
        mindata = [(x[i], f(x[i])) for i in range(1, n) if f(x[i-1]) > f(x[i]) <= f(x[i+1])]
        maxdata = [(x[i], f(x[i])) for i in range(1, n) if f(x[i-1]) < f(x[i]) >= f(x[i+1])]
        if f(x[0]) <= f(x[1]):
            mindata.insert(0, (x[0], f(x[0])))
        if f(x[0]) >= f(x[1]):
            maxdata.insert(0, (x[0], f(x[0])))
        if f(x[-1]) < f(x[-2]):
            mindata.append((x[-1], f(x[-1])))
        if f(x[-1]) > f(x[-2]):
            maxdata.append((x[-1], f(x[-1])))
        Pmin = [i[0] for i in mindata]
        Pmax = [i[0] for i in maxdata]
        Fmin = [i[1] for i in mindata]
        Fmax = [i[1] for i in maxdata]
        return Pmin, Pmax, Fmin, Fmax
    
    def _refine_extrema(self):
        f, a0, b0, n = self.f, self.a, self.b, self.n
        h0 = (b0-a0)/float(n)
        epsilon = 1e-4*h0
        h = 1e-2*epsilon
        df = Derivative(f, h)
        for i, x in enumerate(self.Pmin):
            if x != a0 and x != b0: #Do only for interior points
                a = x-h0
                b = x+h0
                self.Pmin[i], it = self._bisection(df, a, b, epsilon)
        for i, x in enumerate(self.Pmax):
            if x != a0 and x != b0: #Do only for interior points
                a = x-h0
                b = x+h0
                self.Pmax[i], it = self._bisection(df, a, b, epsilon)
        return None
    
    @staticmethod
    def _bisection(f, a, b, eps):
        fa = f(a)
        if fa*f(b) > 0:
            return None, 0
    
        i = 0   # iteration counter
        while b-a > eps:
            i += 1
            m = (a + b)/2.0
            fm = f(m)
            if fa*fm <= 0:
                b = m  # root is in left half of [a,b]
            else:
                a = m  # root is in right half of [a,b]
                fa = fm
        return m, i
    
    def get_global_minimum(self):
        ind = self.Fmin.index(min(self.Fmin))
        return (self.Pmin[ind], self.Fmin[ind])
    
    def get_global_maximum(self):
        ind = self.Fmax.index(max(self.Fmax))
        return (self.Pmax[ind], self.Fmax[ind])
    
    def get_all_minima(self):
        return zip(self.Pmin,self.Fmin)
        
    def get_all_maxima(self):
        return zip(self.Pmax,self.Fmax)
    
class Derivative(object):
    def __init__(self, f, h=1E-5):
        self.f = f
        self.h = float(h)

    def __call__(self, x):
        f, h = self.f, self.h      # make short forms
        return (f(x+h) - f(x))/h
            
    
def f(x):
    #return 2*x + 3
    return x**2 * np.exp(-0.2*x)*np.sin(2*np.pi*x)
    #return -x**2
    #return 0*x + 2
    
if __name__ == '__main__':
    m = MinMax(f, 0, 4, 5000) #Use n=5000 so that n+1 = 5001 equally spaced points
    print '\n', m
    m._refine_extrema()
    print '\n', m
