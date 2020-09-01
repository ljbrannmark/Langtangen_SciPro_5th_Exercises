# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 22:03:28 2020

@author: lars-johan.brannmark
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.close('all')

#Function for generating position and velocity data for time array t
def orbit(a, b, omega, t):
    x = a*np.cos(omega*t)
    y = b*np.sin(omega*t)
    vx = -omega*a*np.sin(omega*t)
    vy = omega*b*np.cos(omega*t)
    return x, y, vx, vy

#Init function for FuncAnimation
def init():
    lines[0].set_data([],[])
    lines[1].set_data([],[])
    return lines

#Frame function for FuncAnimation
def frame(args):
    a, b, omega, t = args
    x, y, vx, vy = orbit(a, b, omega, t)
    v_abs = np.sqrt(vx[-1]**2 + vy[-1]**2)
    
    lines[0].set_data(x, y)
    lines[0].get_figure().gca().set_title('Velocity: %.2f'%v_abs)
    lines[1].set_data(x[-1], y[-1])
    return lines

a = 2
b = 1
omega = 1
n = 100
t = np.linspace(0, 2*np.pi/omega, n+1)
dt = 2*np.pi/(omega*n)

fig = plt.figure()
lines = plt.plot([], [], 'b-', [], [], 'ko')

plt.axis('scaled')
plt.axis(1.25*max(a, b)*np.array([-1, 1, -1, 1]))
plt.xlabel('x')
plt.ylabel('y')

all_args = [(a, b, omega, t[0:i+1]) for i in range(1,n+1)]

anim = FuncAnimation(fig, frame, all_args, interval = np.round(dt*1000), init_func=init, blit=False)

plt.show()