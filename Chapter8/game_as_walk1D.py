# -*- coding: utf-8 -*-
"""
Created on Fri Aug 21 21:41:54 2020

@author: lars-johan.brannmark
"""
# =============================================================================
# Exercise 8.34 a) 
# =============================================================================
#
# Losing 1 Euro = going 1 step to the left, with probability 1-p
# Winning 1 Euro = going 1 step to the right, with probability p
# Start position = x0. Stop position = F

# =============================================================================
# Exercise 8.34 b)
# =============================================================================

import numpy # not as np since np is an important variable here
import matplotlib.pyplot as plt
from math import log

def game_prob_p(p, win_amount=1, lose_amount=-1, size=1):
    return numpy.where(numpy.random.random(size=size) <= p, win_amount, lose_amount)

#With p = 0.49 it Seems practically impossible to reach x_i = 100 for any
#finite value of i. The cumulative sum of +/- 1 outcomes drifts off quickly
#in the negative direction, never to return to positive values (though there
#is,  theoretically, a nonzero pobability that it will). The drift is shown
#in the following plot:

x = numpy.array([10])
for n in range(1,21):
    x = numpy.cumsum(numpy.r_[x[-1], game_prob_p(p=0.49, size=100000)])
    plt.plot(numpy.arange((n-1)*100000+1,n*100000+2), x, 'r')
    plt.show()
    plt.pause(0.1)

#To get down to reasonable exection time, we let p be a number very 
#close to 0.5:
p = 0.5 - 1E-7  #Probability of winning a single game
F = 100  #Target fortune
x_0 = 10 #Start amount

np = 500  #No. of random walks
num_games = numpy.zeros(np, dtype=long)
for i in range(np):
    
    x = numpy.array([x_0], dtype=int)
    xLen = 50000
    n = 0
    while not F in x:
        x = numpy.cumsum(numpy.r_[x[-1], game_prob_p(p, size=xLen)])
        n += 1
    num_games[i] = (n-1)*xLen + numpy.nonzero(x == F)[0][0]
    if i % 50 == 0:
        print 'Number of random walks simulated: %d'%i
    
print 'Average number of games to reach F=100: %d'%num_games.mean()

# =============================================================================
# Exercise 8.34 c)
# =============================================================================
#
# (F-x_0)**r = num_games.mean()
#
r = log(num_games.mean(), F-x_0)

print 'r = %.3f'%r 