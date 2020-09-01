# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 22:15:27 2020

@author: lars-johan.brannmark
"""

import numpy as np

v = np.array([2, 3, -1],'float')

def f(x):
    return x**3 + x*np.exp(x) + 1

fv1 = np.zeros_like(v,'float')
for i in range(len(v)):
    fv1[i] = f(v[i])

fv2 = v**3 + v*np.exp(v) + 1

fv3 = f(v)

fv4 = np.array([f(v_x) for v_x in v])

print(fv1)
print(fv2)
print(fv3)
print(fv4)