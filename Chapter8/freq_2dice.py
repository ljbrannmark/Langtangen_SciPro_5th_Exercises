# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 00:03:06 2020

@author: lars-johan.brannmark
"""

import random
N = 100000

p = {k: [random.randint(1,6)+random.randint(1,6) for i in range(N)].count(k)/float(N)\
      for k in range(2,13)}

eyes = [i+j for i in range(1,7) for j in range(1,7)]
p_exact = {k: eyes.count(k)/float(len(eyes)) for k in range(2,13)}

for k in range(2, 13):
    print 'p(%d) = %f, p_exact(%d) = %f'%(k, p[k], k, p_exact[k])