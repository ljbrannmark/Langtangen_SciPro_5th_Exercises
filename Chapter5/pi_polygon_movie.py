# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 22:53:03 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.close('all')

def pathlength(x, y):
        return sum( np.sqrt( (x[i]-x[i-1])**2 + (y[i]-y[i-1])**2 ) 
                   for i in range(1,len(x)) )
    
def pi_approx(N):
    x = np.array([0.5*np.cos( (2*np.pi*i)/N ) for i in range(N+1)])
    y = np.array([0.5*np.sin( (2*np.pi*i)/N ) for i in range(N+1)])
    pi_app = pathlength(x,y)   
    return pi_app, x, y

def init():
    lines[0].set_data([],[])
    return lines

def frame(args):
    N, lines = args
    pi_app, x, y = pi_approx(N)
    error = np.pi - pi_app
    lines[0].set_data(x, y)
    lines[0].get_figure().gca().set_title('Approx. error: %.4e'%error)
    return lines

K = 100
N_values = range(4, K+1)

fig = plt.figure()
fig.gca().add_artist(plt.Circle((0, 0), 0.5, color='r', fill=False))

lines = plt.plot([],[])
plt.axis('equal')
plt.axis([-0.8, 0.8, -0.8, 0.8])
plt.xlabel('x')
plt.ylabel('y')

all_args = [(N, lines) for N in N_values]

anim = FuncAnimation(fig, frame, all_args, interval = 300, init_func=init, blit=False)

plt.show()




