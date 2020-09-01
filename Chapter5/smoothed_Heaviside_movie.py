# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 22:13:19 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
import glob, os

###############################################################################
###############################################################################
# Approach 1: Create animation from a set of saved .png files:

for filename in glob.glob('tmp*.png'):
    os.remove(filename)
    
plt.close('all')

def H_eps(x, eps=0.01):
    y = np.zeros_like(x)
    cond1 = x < -eps
    cond2 = x > eps
    cond3 = np.logical_and(-eps <= x, x <= eps)
    y[cond1] = 0
    y[cond2] = 1
    y[cond3] = 0.5 + x[cond3]/(2.0*eps) + 1/(2*np.pi)*np.sin(np.pi*x[cond3]/eps)
    return y

x = np.linspace(-1, 1, 1000)
eps_values = np.linspace(2, 0, 61)

plt.ion()
y = H_eps(x, eps_values[0])
lines = plt.plot(x, y)
plt.axis([x[0], x[-1], -0.1, 1.1])
plt.xlabel('x')
plt.ylabel('y')

counter = 0
for eps in eps_values:
    y = H_eps(x, eps)
    lines[0].set_ydata(y)
    plt.legend(['t=%4.2f' % eps])
    plt.draw()
    plt.savefig('tmp_%04d.png' % counter)
    counter += 1


# Animated GIF
cmd = 'convert -delay 16.7 tmp_*.png Heaviside_movie1.gif'
os.system(cmd)

###############################################################################
###############################################################################
# Approach 2: Create animation using FuncAnimation from matplotlib.animation:

from matplotlib.animation import FuncAnimation

plt.close('all')

def H_eps(x, eps=0.01):
    y = np.zeros_like(x)
    cond1 = x < -eps
    cond2 = x > eps
    cond3 = np.logical_and(-eps <= x, x <= eps)
    y[cond1] = 0
    y[cond2] = 1
    y[cond3] = 0.5 + x[cond3]/(2.0*eps) + 1/(2*np.pi)*np.sin(np.pi*x[cond3]/eps)
    return y

def init():
    lines[0].set_data([],[])
    return lines

def frame(args):
    frame_no, eps, x, lines = args
    y = H_eps(x, eps)
    lines[0].set_data(x, y)
    return lines

x = np.linspace(-1, 1, 1000)
eps_values = np.linspace(2, 0, 61)

fig = plt.figure()
lines = plt.plot([],[])
plt.axis([x[0], x[-1], -0.1, 1.1])
plt.xlabel('x')
plt.ylabel('y')

all_args = [(frame_no, eps, x, lines) for frame_no, eps in enumerate(eps_values)]

anim = FuncAnimation(fig, frame, all_args, interval = 50, init_func=init, blit=True)

plt.show()


