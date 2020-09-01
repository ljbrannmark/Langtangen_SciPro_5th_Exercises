# -*- coding: utf-8 -*-
"""
Created on Tue Aug  4 00:22:34 2020

@author: lars-johan.brannmark
"""

import random

N = 10

heads = 0
for i in range(N):
    r = random.randint(0, 1)
    print '%s'%('head' if r==0 else 'tail')
    heads += r==0

print 'Number of heads: %s' %heads