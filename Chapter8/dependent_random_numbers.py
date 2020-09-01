# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 21:50:52 2020

@author: lars-johan.brannmark
"""

import numpy as np

# =============================================================================
# Exercise 8.22 a)
# =============================================================================
N = 50
print ''.join(np.char.asarray(np.random.randint(2, size=N)))

# =============================================================================
#  Exercise 8.22 b)
# =============================================================================
def dependent_binary(N, p):
    r = np.zeros(shape=N, dtype=int)
    r[0] = np.random.randint(2)    
    for i in range(N-1):
        r[i+1] = r[i] if np.random.random() < p else int(not r[i])
    return r

N=50
p = 0.5
print ''.join(np.char.asarray(dependent_binary(N,p)))

# =============================================================================
#  Exercise 8.22 c)
# =============================================================================

N = 80
for p in [0.5, 0.8, 0.9]:
     print ''.join(np.char.asarray(dependent_binary(N,p)))   