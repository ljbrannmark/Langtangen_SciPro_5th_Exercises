# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 00:34:41 2020

@author: lars-johan.brannmark
"""

def random_walk_2D(np, ns, plot_step, barrier):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    xL, xH, yL, yH = barrier
    moves = numpy.random.randint(1, 4+1, size=ns*np)
    moves.shape = (ns, np)

    # Estimate max and min positions
    xymax = 3*numpy.sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    for step in range(ns):
        this_move = moves[step,:]
        ypositions += numpy.where(this_move == NORTH, 1, 0)
        ypositions = numpy.where(ypositions > yH, yH, ypositions)
        ypositions -= numpy.where(this_move == SOUTH, 1, 0)
        ypositions = numpy.where(ypositions < yL, yL, ypositions)
        xpositions += numpy.where(this_move == EAST,  1, 0)
        xpositions = numpy.where(xpositions > xH, xH, xpositions)
        xpositions -= numpy.where(this_move == WEST,  1, 0)
        xpositions = numpy.where(xpositions < xL, xL, xpositions)

        # Just plot every plot_step steps
        if (step+1) % plot_step == 0:
            plot(xpositions, ypositions, 'ko',
                 axis=[1.1*xL, 1.1*xH, 1.1*yL, 1.1*yH],
                 title='%d particles after %d steps' % 
                       (np, step+1),
                 savefig='tmp_%03d.pdf' % (step+1))
            g = get_backend()
            g.show()
            g.pause(0.2)
    return xpositions, ypositions

# Main program
from scitools.std import plot
import numpy, sys
numpy.random.seed(11)

np = int(sys.argv[1])  # number of particles
ns = int(sys.argv[2])  # number of steps
plot_step = int(sys.argv[3])  # plot each plot_step step
xL, xH, yL, yH = (-20, 20, -20, 20)
x, y = random_walk_2D(np, ns, plot_step, (xL, xH, yL, yH))
