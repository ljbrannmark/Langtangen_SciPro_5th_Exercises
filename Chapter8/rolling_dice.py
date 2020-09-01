# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 21:53:31 2020

@author: lars-johan.brannmark
"""

#Exercise 8.5
#
# 1. P(x=6) = 1/6 (approx. 0.1667)
# 2. P(x1=x2=x3=x4=6) = (1/6)**4 = 1/1296 (approx. 0.0007716)
# 3. P(x4=6|x1=x2=x3=6) = 1/6 (approx. 0.1667)
# 4. P(x101=6|x1=...=x100=6) = 1/6, if P(Die is fair)=1.0. BUT:
#    evidence for P(Die is fair) < 1.0 is pretty strong..

import random

def throwdie(m, N):
    #Throw a die with m eyes N times 
    return [random.randint(1,m) for i in range(int(N))]

def p_compute(L, values):
    #Given a list L of integers, compute the relative occurrance of the
    # integer sequence given in values
    values = [values] if not isinstance(values, list) else values
    M = sum([L[i:i+len(values)]==values for i in range(len(L))])
    return float(M)/(len(L)-len(values)+1)

def getnextelem(L, values):
    #Return a sublist of the list L, whose elements are such that the 
    #past len(values) elements in L are equal to values 
    indices = [i+len(values) for i in range(len(L)) if L[i:i+len(values)]==values]
    return [L[indices[i]] for i in range(len(indices))]

N=1e6
#Get list of throwing six-eye die N times:
L = throwdie(6,N)
#Compute probability of getting a six:
p_6 = p_compute(L, 6)
#Compute probability of getting four sixes in a row:
p_6666 = p_compute(L, [6, 6, 6, 6])
#Get the sublist of results that succeed three sixes in a row:
L_666_nextelem = getnextelem(L, [6, 6, 6])
#Compute the probability of a six in that sublist:
p_6_given_666 = p_compute(L_666_nextelem, 6)

print 'Q1: P(x=6) = %g' %p_6
print 'Q2: P(x1=x2=x3=x4=6) = %g' %p_6666
print 'Q3: P(x4=6|x1=x2=x3=6) = %g' %p_6_given_666
