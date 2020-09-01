# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 22:58:38 2019

@author: larsjohan
"""
from math import sqrt, ceil

def primes(n):
    #List of indicators A[0],A[1],...,A[n]
    A = [True]*(n+1) 
    # for i = 2, 3,... , not exceeding sqrt(n)
    for i in range( 2 , int( ceil( sqrt(n) ) ) ):
        if A[i]:
            for j in range(i**2,n+1,i):
                A[j]=False
    P = []
    for i in range(2,n+1):
        if A[i]:
            P.append(i)
    return P