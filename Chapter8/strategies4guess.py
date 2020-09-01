# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:53:36 2020

@author: lars-johan.brannmark
"""

import random
import numpy as np

def guess_game(guessfunc, Lo=1, Hi=100):
    
    number = random.randint(Lo, Hi)
    
    attempts = 0  # count no of attempts to guess the number
    p, q = Lo, Hi #Initialize interval [p, q]
    
    s = guessfunc(p,q)      #Guess a number within [p, q]
    attempts += 1
    while s != number:
        if s < number:     #If guess is too low, let p=s+1
            p = s+1
        elif s > number:   #Else if guess is too high, let q=s-1           
            q = s-1
        s = guessfunc(p, q) #New guess
        attempts += 1

    return attempts
            
N = 100000

#Construct two different guess functions to be compared
f_mp = lambda p, q: int((p+q)/2.0)
f_u = lambda p, q: random.randint(p, q)

mp_attempts = 0
u_attempts = 0
for i in range(N):
    mp_attempts += guess_game(f_mp, Lo=1, Hi=100)
    u_attempts += guess_game(f_u, Lo=1, Hi=100)  

mp_avg = mp_attempts/float(N)
u_avg = u_attempts/float(N)

print 'Average number of attempts for midpoint strategy: %.2f' %mp_avg
print 'Average number of attempts for uniform strategy: %.2f' %u_avg