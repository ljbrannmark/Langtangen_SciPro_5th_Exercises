# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 23:01:56 2019

@author: lars-johan.brannmark
"""

def binomial(x, n, p):
    from math import factorial
    return factorial(n) / (factorial(x)*factorial(n-x)) * p**x*(1-p)**(n-x)

print 'Probability of getting two heads when flipping a coin\
 five times: binomial(2,5,1.0/2) = %g\n' %binomial(2,5,1.0/2)

print 'Probability of getting four ones in a row when throwing a\
 die: binomial(4,4,1.0/6) = %g\n' %binomial(4,4,1.0/6)
 
print 'Probability of breaking a ski during five competitions: \
1-binomial(0,5,1.0/120) = %g\n' %(1-binomial(0,5,1.0/120))