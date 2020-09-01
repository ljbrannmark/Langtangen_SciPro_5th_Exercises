# -*- coding: utf-8 -*-
"""
Created on Sun Aug 23 23:02:19 2020

@author: lars-johan.brannmark
"""

import numpy
import random
import matplotlib.pyplot as plt
import time
from pprint import pformat
from scitools.std import plot

# =============================================================================
# Classes
# =============================================================================

class Particle(object):
    def __init__(self, x, y):
        self.pos = numpy.array([x, y])
        self.t = 0
        
    def __str__(self):
        return "(" + "%d" % self.pos[0] + ", %d" % self.pos[1] + ")"
        
    def __repr__(self):
        return self.__str__()
        
    def move(self):
        self.t += 1
        NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants
        direction = random.randint(1, 4)
        if direction == NORTH:    #Going East
            self.pos[1] += 1
        elif direction == SOUTH:  #Going West
            self.pos[1] -= 1
        elif direction == EAST:  #Going North
            self.pos[0] += 1
        elif direction == WEST:  #Going South
            self.pos[0] -= 1
            
            
class Particles(object):
    def __init__(self, np, plot_step=5):
        self.particles = [Particle(0.0, 0.0) for i in range(np)]
        self.plotstep = plot_step
        
    def __str__(self):
        return pformat([p for p in self.particles])
    
    def __repr__(self):
        return self.__str__()
    
    def move(self):
        for p in self.particles:
            p.move()
        
    def plot(self, axis=[-10, 10, -10, 10]):
        x = [p.pos[0] for p in self.particles]
        y = [p.pos[1] for p in self.particles]
        plt.cla()
        plt.plot(x, y, 'k.')
        plt.axis(axis)
        plt.draw()
        
    def moves(self, ns):
        xymax = 3*numpy.sqrt(ns); xymin = -xymax
        for step in range(ns):
            self.move()
            if (step+1) % self.plotstep == 0:
                self.plot(axis=[xymin, xymax, xymin, xymax])
                plt.pause(0.1)
                
class Particles_vec(object):
    def __init__(self, np, plot_step=5):
        self.particles = numpy.zeros((np, 2),dtype=int)
        self.plotstep = plot_step
        
    def __str__(self):
        return pformat([p for p in zip(self.particles[:,0],self.particles[:,1])])
    
    def __repr__(self):
        return self.__str__()
        
    def plot(self, axis=[-10, 10, -10, 10]):
        plt.cla()
        plt.plot(self.particles[:,0], self.particles[:,1], 'k.')
        #plt.axis('equal')
        plt.axis(axis)
        plt.draw()
        
    def moves(self, ns):
        xymax = 3*numpy.sqrt(ns); xymin = -xymax
        np=len(self.particles[:,0])
        moves = numpy.random.randint(1, 4+1, size=ns*np)
        moves.shape = (ns, np)
        NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants
        
        for step in range(ns):
            this_move = moves[step,:]
            self.particles[:,1] += numpy.where(this_move == NORTH, 1, 0)
            self.particles[:,1] -= numpy.where(this_move == SOUTH, 1, 0)
            self.particles[:,0] += numpy.where(this_move == EAST,  1, 0)
            self.particles[:,0] -= numpy.where(this_move == WEST,  1, 0)
            if (step+1) % self.plotstep == 0:
                self.plot(axis=[xymin, xymax, xymin, xymax])
                plt.pause(0.1)

# =============================================================================
# Functions
# =============================================================================

#For test and comparison, we use this random_walk_2D function from walk2D.py.
def random_walk_2D(np, ns, plot_step):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    # extent of the axis in the plot:
    xymax = 3*numpy.sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    for step in range(ns):
        for i in range(np):
            direction = random.randint(1, 4)
            if direction == NORTH:
                ypositions[i] += 1
            elif direction == SOUTH:
                ypositions[i] -= 1
            elif direction == EAST:
                xpositions[i] += 1
            elif direction == WEST:
                xpositions[i] -= 1

        # Plot just every plot_step steps
        if (step+1) % plot_step == 0:
            plot(xpositions, ypositions, 'ko',
                 axis=[xymin, xymax, xymin, xymax],
                 title='%d particles after %d steps' % 
                       (np, step+1),
                 savefig='tmp_%03d.pdf' % (step+1))
    return xpositions, ypositions

#For test and comparison, we use this vectorized random_walk_2D function from
#walk2Dv.py. (Here named random_walk_2D_vec.)
def random_walk_2D_vec(np, ns, plot_step):
    xpositions = numpy.zeros(np)
    ypositions = numpy.zeros(np)
    moves = numpy.random.randint(1, 4+1, size=ns*np)
    moves.shape = (ns, np)

    # Estimate max and min positions
    xymax = 3*numpy.sqrt(ns); xymin = -xymax

    NORTH = 1;  SOUTH = 2;  WEST = 3;  EAST = 4  # constants

    for step in range(ns):
        this_move = moves[step,:]
        ypositions += numpy.where(this_move == NORTH, 1, 0)
        ypositions -= numpy.where(this_move == SOUTH, 1, 0)
        xpositions += numpy.where(this_move == EAST,  1, 0)
        xpositions -= numpy.where(this_move == WEST,  1, 0)

        # Just plot every plot_step steps
        if (step+1) % plot_step == 0:
            plot(xpositions, ypositions, 'ko',
                 axis=[xymin, xymax, xymin, xymax],
                 title='%d particles after %d steps' % 
                       (np, step+1),
                 savefig='tmp_%03d.pdf' % (step+1))
    return xpositions, ypositions

def test_Particles():
    #Test the class implementation, with the function random_walk_2D
    #from walk2D.py as reference.
    np = 4
    
    success = True
    
    random.seed(10)
    P = Particles(np, plot_step=4)
    P.moves(1)
    xpos_c = numpy.array([P.particles[n].pos[0] for n in range(np)])
    ypos_c = numpy.array([P.particles[n].pos[1] for n in range(np)])
    random.seed(10)
    xpos_f, ypos_f = random_walk_2D(np, 1, plot_step=4)
    success = success and (xpos_c==xpos_f).all() and (ypos_c==ypos_f).all()
    
    random.seed(10)
    P = Particles(np, plot_step=4)
    P.moves(2)
    xpos_c = numpy.array([P.particles[n].pos[0] for n in range(np)])
    ypos_c = numpy.array([P.particles[n].pos[1] for n in range(np)])
    random.seed(10)
    xpos_f, ypos_f = random_walk_2D(np, 2, plot_step=4)
    success = success and (xpos_c==xpos_f).all() and (ypos_c==ypos_f).all()
    
    random.seed(10)
    P = Particles(np, plot_step=4)
    P.moves(3)
    xpos_c = numpy.array([P.particles[n].pos[0] for n in range(np)])
    ypos_c = numpy.array([P.particles[n].pos[1] for n in range(np)])
    random.seed(10)
    xpos_f, ypos_f = random_walk_2D(np, 3, plot_step=4)
    success = success and (xpos_c==xpos_f).all() and (ypos_c==ypos_f).all()
    if success:
        print 'ok'
    msg = 'Error in class Particles'
    assert success, msg
    
def test_Particles_vec():
    #Test the vetorized class implementation, with the function 
    #random_walk_2D from walk2Dv.py as reference. (Here named
    #random_walk_2D_vec.)
    np = 4
    
    success = True
    
    numpy.random.seed(11)
    P = Particles_vec(np, plot_step=4)
    P.moves(1)
    xpos_c = P.particles[:,0]
    ypos_c = P.particles[:,1]
    numpy.random.seed(11)
    xpos_f, ypos_f = random_walk_2D_vec(np, 1, plot_step=4)
    success = success and (xpos_c==xpos_f).all() and (ypos_c==ypos_f).all()
    
    numpy.random.seed(11)
    P = Particles_vec(np, plot_step=4)
    P.moves(2)
    xpos_c = P.particles[:,0]
    ypos_c = P.particles[:,1]
    numpy.random.seed(11)
    xpos_f, ypos_f = random_walk_2D_vec(np, 2, plot_step=4)
    success = success and (xpos_c==xpos_f).all() and (ypos_c==ypos_f).all()
    
    numpy.random.seed(11)
    P = Particles_vec(np, plot_step=4)
    P.moves(3)
    xpos_c = P.particles[:,0]
    ypos_c = P.particles[:,1]
    numpy.random.seed(11)
    xpos_f, ypos_f = random_walk_2D_vec(np, 3, plot_step=4)
    success = success and (xpos_c==xpos_f).all() and (ypos_c==ypos_f).all()
    if success:
        print 'ok'
    msg = 'Error in class Particles_vec'
    assert success, msg
    
def compare_efficiency():
    #Compare the efficiency of the class Particles against the
    #vectorized version of random_walk_2D from walk2D.py. (Here
    #named random_walk_2D_vec.)
    np = 3000
    ns = 400
    plot_step = 2*ns #Choose plot_step so that the plot is never activated
    
    t_c0 = time.clock()
    P = Particles(np, plot_step)
    P.moves(ns)
    t_c1 = time.clock()-t_c0
    
    t_f0 = time.clock()
    random_walk_2D_vec(np, ns, plot_step)
    t_f1 = time.clock()-t_f0

    print 'Elapsed time, test run of class Particles: %g s.' %(t_c1)
    print 'Elapsed time, test run of function random_walk_2D_vec: %g s.' %(t_f1) 

def compare_efficiency_vec():
    #Compare the efficiency of the class Particles against
    # the vectorized version Particles_vec
    np = 3000
    ns = 400
    plot_step = 2*ns #Choose plot_step so that the plot is never activated
    
    t_0 = time.clock()
    P = Particles(np, plot_step)
    P.moves(ns)
    t_1 = time.clock()-t_0
    
    t_v0 = time.clock()
    P = Particles_vec(np, plot_step)
    P.moves(ns)
    t_v1 = time.clock()-t_v0

    print 'Elapsed time, test run of class Particles: %g s.' %(t_1)
    print 'Elapsed time, test run of class Particles_vec: %g s.' %(t_v1) 
    
# =============================================================================
# Test block
# =============================================================================

if __name__ == '__main__':
    print 'Testing class version against random_walk_2D from walk2D.py...'
    test_Particles()
    print 'Testing vectorized class version against random_walk_2D_vec from walk2Dv.py...'
    test_Particles_vec()
    print '\nComparing efficiency of class Particles against random_walk_2D_vec, from walk2Dv.py:'
    compare_efficiency()
    print '\nComparing efficiency of class Particles against the vectorized version Particles_vec:'
    compare_efficiency_vec()
    np = int(raw_input('Test run: No. of particles? '))
    P = Particles_vec(np, plot_step=10)
    P.moves(200)
