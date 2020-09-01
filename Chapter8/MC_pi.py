# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 20:58:51 2020

@author: lars-johan.brannmark
"""

import numpy as np
from math import pi

N = 10**6

x1, x2 = -1, 1
y1, y2 = -1, 1

x = (x2-x1)*np.random.random(N) + x1
y = (y2-y1)*np.random.random(N) + y1

M = np.where(x**2+y**2 < 1, 1, 0).sum()

pi_est = M / float(N) * (x2-x1)*(y2-y1)

error = pi - pi_est

print 'pi estimate: %.6f, error: %.4e'%(pi_est, error)