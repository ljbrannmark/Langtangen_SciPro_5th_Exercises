# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 23:48:06 2020

@author: lars-johan.brannmark
"""
import random

class Hat(object):
    def __init__(self, **colors):
        self.balls = [c for c in colors for i in range(colors[c])]
    
    def __str__(self):
        L = list(set(self.balls))
        s = ''
        for i in range(len(L)):
              s += '%s=%d\n'%(L[i],self.balls.count(L[i]))
        return s

    def draw(self, n):
        #Shuffle a copy of self.balls, and pick the n first elements
        balls = list(self.balls)
        random.shuffle(balls)
        return balls[0:n]
        
h = Hat(blue=6, brown=8, green=3)
N = 100000
s = 0
for i in range(N):
    balls = h.draw(6)
    if balls.count('brown')==2 and balls.count('blue')==2:
        s += 1

print 'Probability is %.6f'%(s/float(N))
    
    
    