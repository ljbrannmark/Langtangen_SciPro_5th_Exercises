# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 00:34:02 2020

@author: lars-johan.brannmark
"""

import random

for i in [1, 2, 3, 6]:
    N = 10**i
    M = 0
    for k in range(N):
        M += 0.5 <= random.random() <= 0.6
    print 'N=%d, M/N=%.6g'%(N,float(M)/N)