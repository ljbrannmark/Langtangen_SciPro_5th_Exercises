# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 15:19:22 2020

@author: lars-johan.brannmark
"""


from scitools.std import plot, get_backend
import numpy, sys
import glob, os
numpy.random.seed(11)

def random_walk_2D(np, ns, plot_step, barrier, wall, hole):
    xL, xH, yL, yH = barrier
    xLw, xHw, yLw, yHw = wall
    xLh, xHh, yLh, yHh = hole
    xpositions = (xHw-xL)*numpy.random.random_sample(size=np) + xL
    ypositions = (yH-yL)*numpy.random.random_sample(size=np) + yL
    xmove = (xH-xL)/200.0
    ymove = (yH-yL)/200.0
    
    moves = numpy.random.randint(1, 4+1, size=ns*np)
    moves.shape = (ns, np)

    # Estimate max and min positions
    xymax = 3*numpy.sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    fname_no = 0
    for step in range(ns):
        #Indices to left-cavity particles
        L_ind = numpy.where(xpositions < xHw)[0]
        #Indices to right-cavity particles
        R_ind = numpy.where(xpositions >= xHw)[0]
        
        this_move_L = moves[step,L_ind]
        this_move_R = moves[step,R_ind]
        
        ypositions[L_ind] += numpy.where(this_move_L == NORTH, ymove, 0)
        ypositions[L_ind] = numpy.where(ypositions[L_ind] > yH, yH, ypositions[L_ind])
        ypositions[L_ind] -= numpy.where(this_move_L == SOUTH, ymove, 0)
        ypositions[L_ind] = numpy.where(ypositions[L_ind] < yL, yL, ypositions[L_ind])
        xpositions[L_ind] += numpy.where(this_move_L == EAST,  xmove, 0)
        xpositions[L_ind] = numpy.where((xpositions[L_ind] > xHw-xmove)*((ypositions[L_ind] < yLh)+(ypositions[L_ind] > yHh)), xHw-xmove, xpositions[L_ind])
        xpositions[L_ind] -= numpy.where(this_move_L == WEST,  xmove, 0)
        xpositions[L_ind] = numpy.where(xpositions[L_ind] < xL, xL, xpositions[L_ind])
        
        ypositions[R_ind] += numpy.where(this_move_R == NORTH, ymove, 0)
        ypositions[R_ind] = numpy.where(ypositions[R_ind] > yH, yH, ypositions[R_ind])
        ypositions[R_ind] -= numpy.where(this_move_R == SOUTH, ymove, 0)
        ypositions[R_ind] = numpy.where(ypositions[R_ind] < yL, yL, ypositions[R_ind])
        xpositions[R_ind] += numpy.where(this_move_R == EAST,  xmove, 0)
        xpositions[R_ind] = numpy.where(xpositions[R_ind] > xH, xH, xpositions[R_ind])
        xpositions[R_ind] -= numpy.where(this_move_R == WEST,  xmove, 0)
        xpositions[R_ind] = numpy.where((xpositions[R_ind] < xHw+xmove)*((ypositions[R_ind] < yLh)+(ypositions[R_ind] > yHh)), xHw+xmove, xpositions[R_ind])

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
ns = 10000
plot_step = 100
barrier = (0.0, 1.0, 0.0, 1.0)
wall = (0.5, 0.5, 0.0, 1.0)
hole = (0.5, 0.5, 0.45, 0.55)
x, y = random_walk_2D(np, ns, plot_step, barrier, wall, hole)

cmd = 'convert -delay 40 tmp_*.pdf movie2.gif'
os.system(cmd)
for filename in glob.glob('tmp*.pdf'):
    os.remove(filename)