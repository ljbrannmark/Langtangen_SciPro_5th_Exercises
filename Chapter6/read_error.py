# -*- coding: utf-8 -*-
"""
Created on Fri May  1 00:46:51 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt

def plotfile(filename):
    with open(filename,'r') as infile:
        lines = infile.readlines()
        epsilon = np.array([float(line.split()[1][:-1]) for line in lines
                        if line.find('epsilon:') != -1])
        exact_error = np.array([float(line.split()[4][:-1]) for line in lines
                        if line.find('epsilon:') != -1])
        n = np.array([int(line.split()[5][2:]) for line in lines
                        if line.find('epsilon:') != -1])
    
    plt.figure()
    plt.semilogy(n, epsilon, label='epsilon')
    plt.semilogy(n, exact_error, label='exact error')
    plt.legend()
    plt.show()
    
plotfile('file.txt')