# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 22:50:09 2020

@author: lars-johan.brannmark
"""

import matplotlib.pyplot as plt
import numpy as np

f2c_approx = lambda F: (F-30.0)/2.0
f2c_exact = lambda F: (F-32.0)*5.0/9.0

F = np.linspace(-20, 120, 100)

C_approx = f2c_approx(F)
C_exact = f2c_exact(F)

plt.figure(1)
plt.plot(F, C_exact, 'b-')
plt.plot(F, C_approx, 'r-')
plt.legend(["Approximation", "Exact"])
plt.show()
