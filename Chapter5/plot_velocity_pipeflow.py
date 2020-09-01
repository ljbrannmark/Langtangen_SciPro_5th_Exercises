# -*- coding: utf-8 -*-
"""
Created on Mon Feb 17 22:48:17 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

##################################################################
#Exercise 5.40 a)
def flow_velocity(r, R, beta, mu0, n):
    v = ( beta/(2.0*mu0) )**(1.0/n) * n/(n + 1.0) \
    * ( R**(1.0 + 1.0/n) - r**(1.0 + 1.0/n) )
    return v

##################################################################
#Exercise 5.40 b)
R = 1.0
beta = 0.02
mu0 = 0.02
n = 0.1

r = np.linspace(0, R, 100)
v = flow_velocity(r, R, beta, mu0, n)

plt.figure()
plt.plot(r, v)
plt.xlabel('r')
plt.ylabel('v(r)')
plt.title('Flow velocity in a pipe')
plt.show()
##################################################################
#Exercise 5.40 c)

def init():
    lines[0].set_data([],[])
    return lines

def frame(args):
    r, R, beta, mu0, n, lines = args
    v = flow_velocity(r, R, beta, mu0, n)
    lines[0].set_data(r, v/v[0])
    lines[0].get_figure().gca().set_title('n= %.2f'%n)
    return lines

R = 1.0
beta = 0.02
mu0 = 0.02

fig = plt.figure()
lines = plt.plot([],[])
plt.axis([0, R, 0, 1.1])
plt.xlabel('x')
plt.ylabel('y')

all_args = [(r, R, beta, mu0, n, lines) for n in np.linspace(1.0,0.01,100)]

anim = FuncAnimation(fig, frame, all_args, interval = 50, init_func=init, blit=False)

plt.show()