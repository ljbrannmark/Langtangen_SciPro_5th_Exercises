# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 21:20:34 2020

@author: lars-johan.brannmark
"""

import numpy as np
from math import pi

N = 10**6

xc, yc = 2.0, 1.0
rc = 4.0

x1, x2 = xc-rc, xc+rc
y1, y2 = yc-rc, yc+rc

x = (x2-x1)*np.random.random(N) + x1
y = (y2-y1)*np.random.random(N) + y1

M = np.where((x-xc)**2+(y-yc)**2 < rc**2, 1, 0).sum()

area_est = M / float(N) * (x2-x1)*(y2-y1) 
pi_est = area_est/rc**2

error = pi - pi_est

print 'pi estimate: %.6f, error: %.4e'%(pi_est, error)