# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 19:32:05 2020

@author: lars-johan.brannmark
"""
import sys
import random

r = int(sys.argv[1])
N = int(sys.argv[2])

s = 0
for n in range(N):
    if sum([random.randint(1, 6) for i in range(4)]) < 9:
        s += r-1
    else:
        s -= 1

p = s/float(N) 
 
print 'r =', r
print 'N =', N
print 'Net profit per game: %g Euro'%p
