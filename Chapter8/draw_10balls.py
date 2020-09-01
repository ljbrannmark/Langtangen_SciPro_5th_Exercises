# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 01:14:03 2020

@author: lars-johan.brannmark
"""

import random

colors = ['red', 'blue', 'yellow', 'purple']
hat = []
for color in colors:
    for i in range(10):
        hat.append(color)

N = 100000
M = 0
for i in range(N):
    random.shuffle(hat)
    balls = hat[0:10]
    M += balls.count('blue') == 2 and balls.count('purple') == 2
print 'Probability:', float(M)/N