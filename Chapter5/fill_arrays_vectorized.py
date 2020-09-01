# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 23:54:04 2020

@author: lars-johan.brannmark
"""

import numpy as np

def h(x):
    return 1.0/np.sqrt(2*np.pi) * np.exp( -x**2 / 2.0 )

x = np.linspace(-4,4,41)
y = h(x)