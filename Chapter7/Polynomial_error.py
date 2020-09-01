# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:18:18 2020

@author: lars-johan.brannmark
"""

class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = coefficients
        
    def __call__(self, x):
        return sum([c*x**i for i, c in enumerate(self.coeff)])
    
    def __add__(self, other):
        maxlength = max(len(self.coeff), len(other.coeff))
        #Extend both lists with zeros to this maxlength, but
        # make copies so that the original objects are not changed
        c1 = self.coeff + [0]*(maxlength - len(self.coeff))
        c2 = other.coeff + [0]*(maxlength - len(other.coeff))
        result_coeff = [0]*maxlength
        for i in range(maxlength):
            result_coeff[i] = c1[i] + c2[i]
        return Polynomial(result_coeff)
    

p1 = Polynomial([1, 2, 3, 4])
p2 = Polynomial([2, 3, 4])
p3 = p2 + p1
x = 10.5

print p1(10.5)+p2(10.5)
print p3(10.5)