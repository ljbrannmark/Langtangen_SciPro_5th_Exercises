# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 00:05:21 2020

@author: lars-johan.brannmark
"""

from scitools.std import *

def animate(tmax, dt, x, function, ymin, ymax, t0=0,
            xlabel='x', ylabel='y', filename='tmp_'):
    t = t0
    counter = 0
    while t <= tmax:
        y = function(x, t)
        plot(x, y, '-',
             axis=[x[0], x[-1], ymin, ymax],
             title='time=%2d h' % (t/3600.0),
             xlabel=xlabel, ylabel=ylabel,
             savefig=filename + '%04d.png' % counter)
        savefig('tmp_%04d.pdf' % counter)
        t += dt
        counter += 1

def T(z, t):
    # T0, A1, A2, k, omega1, omega2, a1, a2 are global variables
    return T0 + A1*exp(-a1*z)*sin(omega1*t - a1*z) + A2*exp(-a1*z)*sin(omega2*t - a2*z)

import glob, os
# Remove old plot files
for filename in glob.glob('tmp_*.png'): os.remove(filename)

T0 = 10      # mean surface temperature in Celsius
P1 = 365*24*60*60
P2 = 24*60*60.    # oscillation period of 24 h (in seconds)
omega1 = 2*pi/P1
omega2 = 2*pi/P2
k = 1E-6      # thermal diffusivity (in m**2/s)
a1 = sqrt(omega1/(2*k))
a2 = sqrt(omega2/(2*k))

dt = P2/10    # time lag
tmax = 10*P2  # 10 days simulation

A1 = 15       # amplitude of the temperature variations (in C)
A2 = 7

D = -(1/min(a1,a2))*log(0.001) # max depth
n = 501      # no of points in the z direction

z = linspace(0, D, n)
animate(tmax, dt, z, T, T0-A1-A2, T0+A1+A2, 0, 'z', 'T')
# Make movie files
os.system('convert -delay 50 tmp_*.png movie.gif')
os.system('avconv -i tmp_%04d.png -r 5 -c:v flv movie.flv')
# Can use ffmpeg instead of avconv
