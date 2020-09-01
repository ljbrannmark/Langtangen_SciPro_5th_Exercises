# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 21:20:40 2020

@author: lars-johan.brannmark
"""

import numpy as np

q = 1.0
n = 4
s = 9
N = 10000000

def s_prob(n, s, N=10000):
    #Compute probability of getting a sum less than s when
    #rolling n six-eyed dice.
    return np.where(np.random.randint(1, 6+1, \
            size=(N, n)).sum(axis=1) < s, 1, 0).sum() / float(N)

p = s_prob(4, 9, N)
print 'p = ', p
print 'A fair game requires r=q/p=%d'%np.ceil(q/p)