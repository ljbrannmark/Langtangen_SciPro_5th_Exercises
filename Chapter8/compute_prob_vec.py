# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:59:42 2020

@author: lars-johan.brannmark
"""

import numpy as np

for i in [1, 2, 3, 6]:
    N = 10**i
    r = np.random.random(size=N)
    M = np.logical_and(r >= 0.5, r <= 0.6).sum()
    print 'N=%d, M/N=%.6g'%(N,float(M)/N)