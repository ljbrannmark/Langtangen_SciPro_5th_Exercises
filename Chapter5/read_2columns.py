# -*- coding: utf-8 -*-
"""
Created on Fri Jan 24 20:31:54 2020

@author: lars-johan.brannmark
"""
import numpy as np
import matplotlib.pyplot as plt

infile = open('xy.dat','r')

x = []
y = []
for line in infile:
    x.append(float(line.split()[0]))
    y.append(float(line.split()[1]))
infile.close()

x = np.array(x)
y = np.array(y)

plt.figure(1)
plt.plot(x,y)

print "y_min = %.2f"  %np.min(y)
print "y_max = %.2f"  %np.max(y)
print "y_mean = %.2f" %np.mean(y)
