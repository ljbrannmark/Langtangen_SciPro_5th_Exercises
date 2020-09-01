# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:12:05 2020

@author: lars-johan.brannmark
"""

from Polynomial import Polynomial
from math import factorial, exp

x = float(raw_input('x='))
input_str = '[' + raw_input('Give comma-separated list of N-values: ') + ']'
N_list = eval(input_str)

print '%10s %14s'%('N','p(x)')
print '-'*25
for N in N_list:
    coeffs = [1.0/factorial(k) for k in range(N+1)]
    p = Polynomial(coeffs)
    print '%10.d %14.10g'%(N,p(x))
    
print '\nExact value of exp(x): %.10g' %exp(x)
