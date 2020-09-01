# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 21:12:01 2020

@author: lars-johan.brannmark
"""

import sys
import numpy as np
from scitools.StringFunction import StringFunction


formula = sys.argv[1]

f = StringFunction(formula)

a = float(sys.argv[2])
b = float(sys.argv[3])
n = eval(sys.argv[4])
fname = sys.argv[5]

X = np.linspace(a, b, n)
Y = np.array([f(x) for x in X])

outfile = open(fname,'w')

for i in range(len(X)):
    outfile.write("%10.4f %10.4f\n"%(X[i],Y[i]))
outfile.close()

