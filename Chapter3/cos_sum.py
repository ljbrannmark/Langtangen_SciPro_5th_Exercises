# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 23:35:13 2019

@author: larsjohan
"""

from math import cos, pi

#Define function for approximation of cos
def C(x, n):
    term = 1
    s = term
    for j in range(1,n+1):
        term = -term * x**2 / ( 2.0*j*(2.0*j-1) )
        s += term
    return s

#Define some vales of x and n
X = [4*pi, 6*pi, 8*pi, 10*pi]
N = [5, 25, 50, 100, 200]

#Print first row of the table
print '    x    ',
for j in range(len(N)):
    print '  %3d    ' %N[j],
print

#Print the values in the table
for i in range(len(X)):
    x = X[i]
    print '%9.4f' %x,
    for j in range(len(N)):
        n = N[j]
        cos_approx = C(x, n)
        cos_exact = cos(x)
        err = cos_exact - cos_approx
        print '%9.2e' %err,
    print
    

