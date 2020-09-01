# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:01:26 2019

@author: lars-johan.brannmark
"""

from math import sin, pi
import sys

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
    
def table(n_values, alpha_values, T):
    print '%6s%6s%14s'%('alpha','n','error   ')
    print 26*'-'
    for alpha in alpha_values:
        t=alpha*T
        for n in n_values:
            e = f(t,T) - S(t,n,T)
            print '%6.3f%6d%14.4e' %(alpha,n,e)
        print
        
__all__ = ['S','f','table']
        
if __name__ == '__main__' and len(sys.argv)==4:
    T = eval(sys.argv[1])
    n_values = eval(sys.argv[2])
    alpha_values = eval(sys.argv[3])
    table(n_values, alpha_values, T)

