# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 23:12:27 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

mu = lambda T: 2.414e-5 * 10**(247.8 / (T + 274.15 - 140))

T = np.array(range(0,100),dtype=float)

plt.figure()
plt.plot(T, mu(T))
plt.xlabel('temperature (C)')
plt.ylabel('viscosity (Pa s)')