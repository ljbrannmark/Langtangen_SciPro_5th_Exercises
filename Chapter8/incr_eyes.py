# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 21:06:27 2020

@author: lars-johan.brannmark
"""

import random

N = 10**6

M = []
for i in range(N):
    m = 2
    previous_throw = random.randint(1, 6)
    current_throw = random.randint(1, 6)
    while current_throw > previous_throw:
        m += 1
        previous_throw = current_throw
        current_throw = random.randint(1, 6)
    M.append(m)

p = {i: M.count(i)/float(N) for i in range(2, 8)}     

for m in p:
    print 'p(m=%d) = %g'%(m, p[m])

print '\nRewards for game to be fair:'
for m in p:
    print 'm=%d: r=%.2f €'%(m, 1.0/p[m])