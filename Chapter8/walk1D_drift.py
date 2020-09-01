# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 23:45:00 2020

@author: lars-johan.brannmark
"""

import random
import numpy

np = int(raw_input('np = ? '))  # no. of particles, get value from command line
ns = 100                        # no of steps
r = 0.6                         # Probability of going to the right

positions = numpy.zeros(np)     # all particles start at x=0
HEAD = 1;  TAIL = 2             # constants

for step in range(ns):
    for p in range(np):
        # flip coin: P(HEAD) = r, P(TAIL) = 1-r
        coin = 1 + int(random.random() > r) 
        if coin == HEAD:
            positions[p] += 1   # one unit length to the right
        elif coin == TAIL:
            positions[p] -= 1   # one unit length to the left

print 'Average position: %g, theoretical: %g' \
%(sum(positions)/float(np), r*ns - (1-r)*ns)