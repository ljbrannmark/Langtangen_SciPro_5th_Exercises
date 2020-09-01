# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 12:51:30 2020

@author: lars-johan.brannmark
"""
#Code for Exercise 8.46 a), b) and c)

import numpy as np
import matplotlib.pyplot as plt

#We have, theoretically (holds only approximately for the data):
# sigma_dE = sigma_E*np.sqrt(1+1)/(2*h)
# sigma_d2E = sigma_E*np.sqrt(1+4+1)/h**2
#
# NOTE: In exercise 8.46 it is stated that
# sigma_d2E = sigma_E*2/h**2. This is wrong. 

# Re-use code from Exercise 8.45:

A = 1
T = 2*np.pi
h = T/40.0
n = 200
i = np.arange(n+1)

t = i*h
etabar = A*np.sin(2*np.pi/T*t)

sigma_E = 0.04*A
E = np.random.normal(loc=0.0, scale=sigma_E, size=etabar.size)

eta = etabar + E

j = i[1:-1]
detabar = (etabar[j+1]-etabar[j-1])/(2*h)

dE = (E[j+1]-E[j-1])/(2*h) 

m_dE = dE.mean()
sigma_dE = dE.std()

d2etabar = (etabar[j+1]-2*etabar[j]+etabar[j-1])/(h**2)
d2E = (E[j+1]-2*E[j]+E[j-1])/(h**2)

m_d2E = d2E.mean()
sigma_d2E = d2E.std()

#Theoretical factors:
factor_dE = np.sqrt(2)/(2*h)
factor_d2E = np.sqrt(6)/h**2

print 'Velocity computation: Noise is magnified by a\
 factor of %g.' %(factor_dE)
print 'Experimentally computed factor, using data: %g.' %(sigma_dE/E.std())
print
print 'Acceleration computation: Noise is magnified by a\
 factor of %g.'%(factor_d2E)
print 'Experimentally computed factor, using data: %g.' %(sigma_d2E/E.std())

# =============================================================================
# Exercise 8.46 c)
# =============================================================================

# Re-using code from Exercise 8.44:

with open('gauge.dat') as infile:
    eta = np.array([float(line) for line in infile])
    
n = len(eta)-1 #eta = [eta_0, eta_1, ..., eta_n]
h = 1/300.0
t = np.array([i*h for i in range(n+1)])

v = np.array([(eta[i+1]-eta[i-1])/(2*h) for i in range(1, n)])
a = np.array([(eta[i+1]-2*eta[i]+eta[i-1])/(h**2) for i in range(1, n)])

plt.figure()
plt.plot(t[1:n],v)
plt.xlabel('$t$ [$s$]')
plt.ylabel('$v$ [$m/s$]')

plt.figure()
plt.plot(t[1:n],a)
plt.xlabel('$t$ [s]')
plt.ylabel('$a$ [$m/s^2$]')

def filter_1(eta):
    return np.array([eta[0]]+[0.25*(eta[i+1]+2*eta[i]+eta[i-1]) for i in range(1,len(eta)-1)]+[eta[-1]])

def filter_k(eta, k):
    y = np.array(eta, copy=True)
    for i in range(k):
        y = filter_1(y)
    return y        

eta_1 = filter_k(eta,1)
eta_10 = filter_k(eta,10)
eta_100 = filter_k(eta,100)

v_1 = np.array([(eta_1[i+1]-eta_1[i-1])/(2*h) for i in range(1, n)])
v_10 = np.array([(eta_10[i+1]-eta_10[i-1])/(2*h) for i in range(1, n)])
v_100 = np.array([(eta_100[i+1]-eta_100[i-1])/(2*h) for i in range(1, n)])

a_1 = np.array([(eta_1[i+1]-2*eta_1[i]+eta_1[i-1])/(h**2) for i in range(1, n)])
a_10 = np.array([(eta_10[i+1]-2*eta_10[i]+eta_10[i-1])/(h**2) for i in range(1, n)])
a_100 = np.array([(eta_100[i+1]-2*eta_100[i]+eta_100[i-1])/(h**2) for i in range(1, n)])

# Compute the theoretical noise levels:
std_dE = 1E-4 * np.sqrt(2)/(2*h)
std_d2E = 1E-4 * np.sqrt(6)/(h**2)

print
print 'Theoretical noise level for velocity: %g \n\
(visually consistent with noise level in velocity plot).'%std_dE
print
print 'Theoretical noise level for acceleration: %g \n\
(visually consistent with noise level in acceleration plot)'%std_d2E