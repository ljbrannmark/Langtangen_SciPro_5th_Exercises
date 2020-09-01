# -*- coding: utf-8 -*-
"""
Created on Sun Feb 16 21:44:41 2020

@author: lars-johan.brannmark
"""

from scitools.std import movie
import numpy as np
import matplotlib.pyplot as plt
from math import factorial

##########################################################################
# Exercise 5.39 a) Define function animate_series
def animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact, fname):
    # Remove old plot files
    import glob, os
    for filename in glob.glob('tmp_*.png'): os.remove(filename)
    ###
    x = np.linspace(xmin, xmax, n, dtype='float')
    s = np.zeros_like(x)
    y = exact(x)
    ###
    plt.ion()
    lines = plt.plot([],[],[],[])
    plt.axis([xmin, xmax, ymin, ymax])
    plt.xlabel('x')
    plt.ylabel('y')
    lines[0].set_data(x,y)
    lines[1].set_xdata(x)
    ###
    counter = 0
    for k in range(M,N+1):
        s += fk(x, k)
        lines[1].set_ydata(s)
        plt.savefig('tmp_%04d.png' % counter)
        counter += 1
    # .gif movie (via scitools.easyviz.movie)
    movie('tmp_*.png', encoder='convert', fps=4,
          output_file='%s.gif' % fname)  # play in .gif file

##########################################################################
# Exercise 5.39 b)
fk = lambda x, k: (-1.0)**k * x**(2.0*k+1) / float(factorial(2*k+1))
exact = lambda x: np.sin(x)

M = 0
N = 40
xmin = 0.0
xmax = 13*np.pi
ymin = -2.0
ymax = 2.0
n = 1000

plt.close('all')    
animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact, 'tmpmovie_a')

##########################################################################
# Exercise 5.39 c)
fk = lambda x, k: (-x)**k / float(factorial(k))
exact = lambda x: np.exp(-x)

M = 0
N = 30
xmin = 0.0
xmax = 15.0
ymin = -0.5
ymax = 1.4
n = 1000

plt.close('all') 
animate_series(fk, M, N, xmin, xmax, ymin, ymax, n, exact, 'tmpmovie_b')


