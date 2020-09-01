# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 23:47:22 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def S(t,n,T=2*np.pi):
    s = np.zeros_like(t)
    for i in range(1,n+1):
        s += 1.0/(2*i - 1) * np.sin( 2*(2*i - 1)*np.pi*t / T )
    s = 4.0/np.pi * s
    return s

def f(t, T = 2*np.pi):
    y = np.zeros_like(t)
    cond1 = np.logical_and(0 < t, t < T/2.0 )
    cond2 = t == T/2.0
    cond3 = np.logical_and(T/2.0 < t, t < T )
    y[cond1] = 1.0
    y[cond2] = 0.0
    y[cond3] = -1.0
    return y

def init():
    lines[0].set_data([],[])
    return lines

def frame(args):
    n, lines = args
    y = S(t, n, T)
    lines[0].set_data(t, y)
    lines[0].get_figure().gca().set_title('n= %.2f'%n)
    return lines

#T and t are global variables
T = 2*np.pi
t = np.linspace(0, T, 1000)

fig = plt.figure()
lines = plt.plot([],[],label='Sine sum')
plt.plot(t,f(t),label='Exact')
plt.axis([0, T, -1.25, 1.25])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

all_args = [(n, lines) for n in range(1, 201)]

anim = FuncAnimation(fig, frame, all_args, interval = 200, init_func=init, blit=False)
