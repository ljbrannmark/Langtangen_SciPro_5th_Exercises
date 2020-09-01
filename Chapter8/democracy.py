# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 00:29:24 2020

@author: lars-johan.brannmark
"""

import numpy as np
import scipy.stats as st
import matplotlib.pyplot as plt

########################################################
# Exercise 8.19 a)
def homogeneous(p, N):
    #Return True if the majority are correct, otherwise False
    return (np.random.random(size=N) < p).sum() > N/2.0

def homogeneous_ex():
    #Print a table of when majority are correct, for the 
    # different cases. 1 means majority are correct, 0 means
    # majority are wrong.
    print '       N |    p |             Results '
    print '---------+------+---------------------'
    for N in [5, 1000000]:
        for p in [0.49, 0.51, 0.8]:
            print ' %7d | %4.2f |'%(N,p),
            for i in range(10):
                print '%d'%(int(homogeneous(p, N))),
            print
            
homogeneous_ex()

########################################################
#Exercise 8.19 b)
N = 1000000
# p is the competence level for one person, modeled as a
# probability between 0 and 1
p = np.linspace(0, 1, 100001)
#Move the points 0 and 1 slightly, to avoid zero variance
# in the pdf of M
p[0] += 1e-6
p[-1] -= 1e-6
# p_majority is the probability that the majority of N 
# people are correct in one question:
p_majority = 1.0 - st.norm.cdf(N/2.0, loc=N*p, scale=np.sqrt(N*p*(1-p)))
plt.figure()
plt.plot(p, p_majority)
plt.xlabel('p')
plt.ylabel('1-$\Phi(N/2)$')
plt.title('Probability of majority M>N/2 being\n correct as a function of competence p')
plt.show()
# p_majority**5 is the probability that the majority have
# all five right. If p_majority > 0.9, the majority has
# 90 percent chance of having all five right. This happens
# when p of the population is:
p_population_90 = p[np.where(p_majority**5 > 0.9)[0][0]]

# p**5 is the probability that one person (e.g. the king)
# has all five right. This happens when p of the king is
p_king_90 = 0.9**(1/5.0)

print '-'*40
print 'Required p for population to have all five \n\
right with 90 percent certainty: %g\n' %p_population_90

print 'Required p for the king to have all five \n\
right with 90 percent certainty: %g' %p_king_90
print '-'*40
########################################################
#Exercise 8.19 c)
def heterogeneous(p, N, s):
    #Return True if the majority are correct, otherwise False.
    #Competence level is here modeled as a Gaussian r.v. with
    #mean p and standard deviation s
    return (np.random.random(size=N) < \
            np.random.normal(loc=p, scale=s, size=N)).sum() > N/2.0

def heterogeneous_ex():
    #Print a table of when majority are correct, for the 
    # different cases. 1 means majority are correct, 0 means
    # majority are wrong.
    print '       N |    p |             Results '
    print '---------+------+---------------------'
    for N in [5, 1000000]:
        for p in [0.49, 0.51, 0.8]:
            print ' %7d | %4.2f |'%(N,p),
            for i in range(10):
                print '%d'%(int(heterogeneous(p, N, 0.2))),
            print
            
heterogeneous_ex()

########################################################
#Exercise 8.19 d)

def extremes(p):
    if isinstance(p, (int,float)):
        p = [p]
    for pp in p:
        s = np.linspace(0.1, 0.6, 1001)
        plt.plot(s, st.norm.cdf(-pp/s), label='p=%g : P(Always wrong)'%pp)
        plt.plot(s, 1-st.norm.cdf((1-pp)/s), label='p=%g : P(Always right)'%pp)
        plt.xlabel('s')
        plt.legend()
        plt.show()

plt.figure()
extremes([0.30, 0.60]) #What values of p should be chosen for the plot?

