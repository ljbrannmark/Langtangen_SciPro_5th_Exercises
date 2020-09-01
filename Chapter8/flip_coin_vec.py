# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 21:43:49 2020

@author: lars-johan.brannmark
"""
import numpy as np

N = 10000

#Heads = 0, Tails = 1
n_tails = np.where(np.random.random(size=N)<=0.5, 1, 0).sum()

print 'Number of tails when flipping a coin %d times: %d' %(N, n_tails)