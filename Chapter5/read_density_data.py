# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 21:35:54 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def load2columns(filename):
    infile = open(filename,'r')
    T = []
    D = []
    for line in infile:
        #Do only for lines that can be split into two columns:
        if len(line.split())==2:
            try:
                t = float(line.split()[0])
                d = float(line.split()[1])
                T.append(t)
                D.append(d)
            except ValueError:
                #If conversion to floats fails, then skip and print out the line: 
                print "Skipping line: %s"%line
    infile.close()
    T = np.array(T)
    D = np.array(D)
    return T, D

T, D = load2columns('density_water.dat')

plt.figure()
plt.plot(T,D,'bo')
plt.xlabel('temp $[^\circ C]$')
plt.ylabel('density [$kg/m^3$]')
plt.show()