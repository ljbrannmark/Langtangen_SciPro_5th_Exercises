# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 23:54:47 2019

@author: larsjohan
"""

from math import sqrt
for n in range(1,60):
    r=2.0
    for i in range(n):
        r=sqrt(r)
        if n==52:
            print r,
    for i in range(n):
        r=r**2
        if n==52:
            print r,
    print '%d times sqrt and **2: %.16f' %(n,r)