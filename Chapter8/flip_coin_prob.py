# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 22:52:07 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
import time

# =============================================================================
# Exercise 8.23 a)
# =============================================================================
N = 1000
#Flip a coin N times. 1 is heads, 0 is tails:
c = np.random.randint(2, size=N)

# =============================================================================
# Exercise 8.23 b)
# =============================================================================
for N1 in [10, 100, 500, 1000]:
    #For each N1, select a new subset of outcomes to compute M1/N1
    M1 = np.sum(np.random.choice(c, N1, replace=False))
    print 'Estimated probability when N1=%d: %g'%(N1,M1/float(N1))

# =============================================================================
# Exercise 8.23 c)
# =============================================================================
def prob_head(N):
    r = np.random.random(size=N)
    h = np.where(r <= 0.5, 1, 0)
    p = np.zeros(N)
    for i in range(N):
        p[i] = np.sum(h[:i+1])/float(i+1)
    return p
    
# =============================================================================
# Exercise 8.23 d)
# =============================================================================
def prob_head_vec(N):
    r = np.random.random(size=N)
    h = np.where(r <= 0.5, 1, 0)
    q = np.cumsum(h)/np.arange(1, N+1, dtype=float)
    return q

# =============================================================================
# Exercise 8.23 e)
# =============================================================================
def prob_head_test():
    N = 1000
    np.random.seed(1)
    p1 = prob_head(N)
    np.random.seed(1)
    p2 = prob_head_vec(N)
    msg = 'prob_head(N) and prob_head_vec(N) give different results!'
    success = np.allclose(p1, p2)
    assert success, msg

prob_head_test() 

# =============================================================================
# Exercise 8.23 f)
# =============================================================================
def prob_head_timecmp(N):
    c = time.clock()
    p1 = prob_head(N)
    t1 = time.clock() - c
    c = time.clock()
    p2 = prob_head_vec(N)
    t2 = time.clock() - c
    print 'prob_head_vec(%d) is %g times faster than prob_head(%d)'%(N,t1/t2,N)
    
prob_head_timecmp(N)    

# =============================================================================
# Exercise 8.23 g)
# =============================================================================
N = 10000
I = np.arange(1, N+1, dtype=float)
p = prob_head_vec(N)
plt.plot(I, p)
plt.xlabel('$N_1$')
plt.ylabel('$p$')
plt.title('Estimated probability $p$ of getting a head,\n versus number of coin flips $N_1$')
