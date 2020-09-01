# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 23:40:43 2020

@author: lars-johan.brannmark
"""

import sys
import random

n = int(sys.argv[1])
N = int(sys.argv[2])

M = 0
for i in range(N):
    throw_n = [random.randint(1, 6) for k in range(n)]
    M += throw_n.count(6) >= 1

p_6 = float(M)/N

print 'Probability of at least one six when throwing %d dice: %g' %(n,p_6)