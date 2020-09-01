# -*- coding: utf-8 -*-
"""
Created on Fri Aug  7 22:18:09 2020

@author: lars-johan.brannmark
"""

import numpy as np

def s_prob(n, s, N=10000):
    #Compute probability of getting a sum less than s when
    #rolling n six-eyed dice.
    return np.where(np.random.randint(1, 6+1, \
            size=(N, n)).sum(axis=1) < s, 1, 0).sum() / float(N)

def test_s_prob():
    p0 = s_prob(4, 4, 10000)
    p1 = s_prob(4, 25, 10000)
    success = p0 == 0.0 and p1 == 1.0
    msg = 'Error in function s_prob'
    assert success, msg
    
    n = 2
    N = 4
    s = 9
    np.random.seed(1)
    # This seed gives first random integers 6,4,5,1,2,4,6,1
    # and thus the four outcomes are 6+4=10, 5+1=6, 2+4=6, 6+1=7, of 
    # which 3 are less than 9. So the manually calculated probability
    # is 3.0/4 = 0.75    
    p_manual = 0.75
    p_computed = s_prob(n, s, N)
    success = p_manual == p_computed
    assert success, msg

test_s_prob()