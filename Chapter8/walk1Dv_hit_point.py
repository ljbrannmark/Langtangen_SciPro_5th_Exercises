# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 16:29:00 2020

@author: lars-johan.brannmark
"""

#Exercise 8.33

import numpy # not as np since np is an important variable here

numpy.random.seed(11)

xp = int(raw_input('xp = ? '))
np = 1

x_0 = 0
x = numpy.array([x_0])

xLen = 100000
n = 0
while not xp in x:
    x = numpy.cumsum(numpy.r_[x[-1], 2*numpy.random.randint(1, 2+1, xLen) - 3])
    n += 1

num_steps = (n-1)*xLen + numpy.nonzero(x == xp)[0][0]

print 'It took %d steps for particle to reach the point x=xp=%d.'%(num_steps, xp)