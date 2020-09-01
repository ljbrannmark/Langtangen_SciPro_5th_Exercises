# -*- coding: utf-8 -*-
"""
Created on Fri Jul 12 23:15:33 2019

@author: larsjohan
"""

from math import sin, pi

def S(t,n,T):
    s=0
    for i in range(1,n+1):
        s += 1.0/(2*i - 1) * sin( 2*(2*i - 1)*pi*t / T )
    s = 4.0/pi * s
    return s

def f(t, T):
    if 0 < t < float(T)/2:
        return 1
    if t == float(T)/2:
        return 0
    if float(T)/2 < t < T:
        return -1
    
nList = [1, 3, 5, 10, 30, 100]
alphaList = [0.01, 0.25, 0.49]
T=2*pi

print '%6s%6s%14s'%('alpha','n','error   ')
print 26*'-'
for alpha in alphaList:
    t=alpha*T
    for n in nList:
        e = f(t,T) - S(t,n,T)
        print '%6.3f%6d%14.4e' %(alpha,n,e)
    print