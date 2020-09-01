# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 22:45:57 2020

@author: lars-johan.brannmark
"""

import random
from math import sqrt

N = 10000

hat = ['red']*5 + ['yellow']*5 + ['green']*3 + ['brown']*7

ipp = {}  #Net income per play
p_win = {}  #Probability of winning

for n in range(4, 10+1):
    ### Option 1
    capital = 0
    wins = 0
    r = 60
    for i in range(N):
        capital -= 2*n
        random.shuffle(hat)
        balls = hat[0:n]
        if balls.count('red') == 3:
            capital += r
            wins += 1
    ipp['Opt=1, n=%d'%n] = capital/float(N)
    p_win['Opt=1, n=%d'%n] = wins/float(N)
    
    ### Option 2
    capital = 0
    wins = 0
    r = 7.0 + 5.0*sqrt(n)
    for i in range(N):
        capital -= 2*n
        random.shuffle(hat)
        balls = hat[0:n]
        if balls.count('brown') >= 3:
            capital += r
            wins += 1
    ipp['Opt=2, n=%d'%n] = capital/float(N)
    p_win['Opt=2, n=%d'%n] = wins/float(N)
    
    ### Option 3
    capital = 0
    wins = 0
    r = n**3 - 26
    for i in range(N):
        capital -= 2*n
        random.shuffle(hat)
        balls = hat[0:n]
        if balls.count('yellow') == 1 and balls.count('brown') == 1:
            capital += r
            wins += 1
    ipp['Opt=3, n=%d'%n] = capital/float(N)
    p_win['Opt=3, n=%d'%n] = wins/float(N)
    
    ### Option 4
    capital = 0
    wins = 0
    r = 23
    for i in range(N):
        capital -= 2*n
        random.shuffle(hat)
        balls = hat[0:n]
        if balls.count('red') >= 1 and balls.count('yellow') >= 1 and \
        balls.count('green') >= 1 and balls.count('brown') >= 1:
            capital += r
            wins += 1
    ipp['Opt=4, n=%d'%n] = capital/float(N)
    p_win['Opt=4, n=%d'%n] = wins/float(N)

print 'Profitable games: ', [key for key in ipp if ipp[key] > 0]
print 'Most profitable game: ', max(ipp, key=ipp.get)
    
    
    
    