# -*- coding: utf-8 -*-
"""
Created on Thu Aug 27 22:08:52 2020

@author: lars-johan.brannmark
"""
import random

def simulate(m, n, p, q, b):
    cost = n*p
    correct_guesses = sum([random.random() < b for i in range(n)])
    reward = correct_guesses*q
    return correct_guesses, reward-cost

#(What is the relevance of m, the number of brands?)

n = 4
m = 4
p = 3
q = 6
b = 1.0/4

C = 0
M = 0
N = 100000
for i in range(N):
    correct, money = simulate(m, n, p, q, b)
    C += correct == n
    M += money

print
print 'm=%d, n=%d, p=%d, q=%d, b=%g:' %(m, n, p, q, b)
print 'Average earnings: %.4g, Probability of full score: %.4g'%(M/float(N),C/float(N))

n = 4
m = 4
p = 3
q = 6
b = 1.0/2

C = 0
M = 0
N = 100000
for i in range(N):
    correct, money = simulate(m, n, p, q, b)
    C += correct == n
    M += money

print
print 'm=%d, n=%d, p=%d, q=%d, b=%g:' %(m, n, p, q, b)
print 'Average earnings: %.4g, Probability of full score: %.4g'%(M/float(N),C/float(N))