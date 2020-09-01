# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 22:26:15 2020

@author: lars-johan.brannmark
"""
import time
import numpy as np

c0 = time.clock()

N = 10**8
arraysize = 2**24

rest = N % arraysize
batch_sizes = [arraysize]*(N//arraysize) + [rest]

s = 0
for N_b in batch_sizes:
    #Throw 7 dice N_b times:
    s += (np.random.randint(1, 7, (N_b, 7)).sum(axis=1)==42).sum()
    # Another possibility (slightly slower) could be:
    # s += (np.random.randint(1, 7, (N_b, 7)) == 6).all(axis=1).sum()


print 'P(All sixes when throwing 7 dice) = %e'%(s/float(N))
print 'Theoretical value: %e' %(1/6.0**7)

print '\nElapsed time: %g s.' %(time.clock()-c0)