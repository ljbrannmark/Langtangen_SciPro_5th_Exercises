# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 12:07:21 2020

@author: lars-johan.brannmark
"""

from scitools.std import plot, get_backend
import numpy, sys
import glob, os
numpy.random.seed(11)

def random_walk_2D(np, ns, plot_step, barrier):
    xL, xH, yL, yH = barrier
    xpositions = 0.5*(xH-xL)*numpy.random.random_sample(size=np) + xL
    ypositions = (yH-yL)*numpy.random.random_sample(size=np) + yL
    xmove = (xH-xL)/100.0
    ymove = (yH-yL)/100.0
    
    moves = numpy.random.randint(1, 4+1, size=ns*np)
    moves.shape = (ns, np)

    # Estimate max and min positions
    xymax = 3*numpy.sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    fname_no = 0
    for step in range(ns):
        this_move = moves[step,:]
        ypositions += numpy.where(this_move == NORTH, ymove, 0)
        ypositions = numpy.where(ypositions > yH, yH, ypositions)
        ypositions -= numpy.where(this_move == SOUTH, ymove, 0)
        ypositions = numpy.where(ypositions < yL, yL, ypositions)
        xpositions += numpy.where(this_move == EAST,  xmove, 0)
        xpositions = numpy.where(xpositions > xH, xH, xpositions)
        xpositions -= numpy.where(this_move == WEST,  xmove, 0)
        xpositions = numpy.where(xpositions < xL, xL, xpositions)

        # Just plot every plot_step steps
        if (step+1) % plot_step == 0:
            fname_no += 1
            plot(xpositions, ypositions, 'k.',
                 axis=[xL-0.1*(xH-xL), xH+0.1*(xH-xL), yL-0.1*(yH-yL), yH+0.1*(yH-yL)],
                 title='%d particles after %d steps' % 
                       (np, step+1),
                 savefig='tmp_%03d.pdf' % (fname_no))
            g = get_backend()
            g.show()
            g.pause(0.01)
    return xpositions, ypositions

# Main program


np = 10000
ns = 5000
plot_step = 50
xL, xH, yL, yH = (0.0, 1.0, 0.0, 1.0)
x, y = random_walk_2D(np, ns, plot_step, (xL, xH, yL, yH))

cmd = 'convert -delay 40 tmp_*.pdf movie.gif'
os.system(cmd)
for filename in glob.glob('tmp*.pdf'):
    os.remove(filename)