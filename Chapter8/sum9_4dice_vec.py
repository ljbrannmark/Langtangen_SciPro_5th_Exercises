# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 13:02:57 2020

@author: lars-johan.brannmark
"""
import sys
import numpy as np

r = int(sys.argv[1])
N = int(sys.argv[2])
 
p = np.where(np.random.randint(1, 7, size=(4, N)).sum(axis=0) < 9, \
             r-1, -1).sum() / float(N)

print 'r =', r
print 'N =', N
print 'Net profit per game: %g Euro'%p