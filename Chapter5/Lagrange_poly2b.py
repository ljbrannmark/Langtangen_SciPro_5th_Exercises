# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 22:00:04 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
import Lagrange_poly2 as lg
 
f = lambda x: abs(x)
plt.figure()
for n in [2, 4, 6, 10]:
    lg.graph(f, n, -2, 2, resolution=1001)
    
plt.figure()
for n in [13, 20]:
    lg.graph(f, n, -2, 2, resolution=1001)    