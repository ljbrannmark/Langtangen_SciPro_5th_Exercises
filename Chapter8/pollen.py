# -*- coding: utf-8 -*-
"""
Created on Sat Aug 22 23:31:47 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# =============================================================================
# Exercise 8.35 a)
# =============================================================================

def pollen_2D_walk(n_steps, n_particles, m=0, std=0.05):
    """
    Model a 2D random walk of pollen particles in a number of 
    time steps, starting at position (x, y) = (0, 0). The steps
    in x, y directions are modeled as Gaussian i.i.d. r.v.'s with
    mean m and standard deviation std.
    
    Output: A numpy array of size (n_steps x n_particles x 2).
    
    Time steps are along dimension 0
    Particles are along dimension 1
    x and y coordinates are along dimension 2
    """
    return np.cumsum( \
        np.concatenate( \
            ( np.zeros((1, n_particles, 2)), \
             np.random.normal(loc=m, scale=std, size=(n_steps, n_particles, 2)) )\
             , axis=0), \
        axis=0 )
            
# =============================================================================
# Exercise 8.35 b)
# =============================================================================

# Generate random walk data for 1000 particles evolving in 100 time steps:
n_particles = 1000
n_steps = 100
X = pollen_2D_walk(n_steps, n_particles)

# Define init and frame functions for FuncAnimation
def init():
    lines[0].set_data([],[])
    lines[0].set_marker('.')
    lines[0].set_linestyle('None')
    return lines

def frame(args):
    frame_no, x, lines = args
    lines[0].set_data(x[:,0],x[:,1])
    lines[0].get_figure().gca().set_title('Time: %d s.'%frame_no)
    return lines

fig = plt.figure()
lines = plt.plot([],[])
plt.axis('equal')
plt.axis([-1.8, 1.8, -1.8, 1.8])
plt.xlabel('x')
plt.ylabel('y')

all_args = [(i, X[i,:,:], lines) for i in range(len(X[:,1,1]))]
anim = FuncAnimation(fig, frame, all_args, interval = 1000, init_func=init, blit=False)
plt.show()

# =============================================================================
# Exercise 8.35 c)
# =============================================================================

# Plot the average distance of the particles from the origin
t = np.array(range(len(X[:,1,1])))
avg_dist = np.mean(np.linalg.norm(X, 2, axis=2), axis=1)
plt.figure()
plt.plot(t, avg_dist)
plt.xlabel('Time [s]')
plt.ylabel('Distance [mm]')
plt.title('Average particle distance from the origin\n as a function of time')
