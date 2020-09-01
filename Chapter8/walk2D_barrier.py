# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 23:43:29 2020

@author: lars-johan.brannmark
"""

def random_walk_2D(np, ns, plot_step, barrier):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    xL, xH, yL, yH = barrier
    # extent of the axis in the plot:
    xymax = 3*numpy.sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    for step in range(ns):
        for i in range(np):
            direction = random.randint(1, 4)
            if direction == NORTH and ypositions[i] < yH:
                ypositions[i] += 1
            elif direction == SOUTH and ypositions[i] > yL:
                ypositions[i] -= 1
            elif direction == EAST and xpositions[i] < xH:
                xpositions[i] += 1
            elif direction == WEST and xpositions[i] > xL:
                xpositions[i] -= 1

        # Plot just every plot_step steps
        if (step+1) % plot_step == 0:
            plot(xpositions, ypositions, 'ko',
                 axis=[xymin, xymax, xymin, xymax],
                 title='%d particles after %d steps' % 
                       (np, step+1),
                 savefig='tmp_%03d.pdf' % (step+1))
            g = get_backend()
            g.show()
            g.pause(0.2)
    return xpositions, ypositions

# main program:
import random
random.seed(10)
import sys
import numpy
from scitools.std import plot, get_backend

np        = int(sys.argv[1])  # number of particles
ns        = int(sys.argv[2])  # number of steps
plot_step = int(sys.argv[3])  # plot every plot_step steps
xL, xH, yL, yH = (-30, 30, -30, 30)
x, y = random_walk_2D(np, ns, plot_step, (xL, xH, yL, yH))
