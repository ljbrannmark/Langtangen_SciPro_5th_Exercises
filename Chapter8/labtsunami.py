# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:48:35 2020

@author: lars-johan.brannmark
"""
import numpy as np
import matplotlib.pyplot as plt

with open('gauge.dat') as infile:
    eta = np.array([float(line) for line in infile])
    
n = len(eta)-1 #eta = [eta_0, eta_1, ..., eta_n]
h = 1/300.0
t = np.array([i*h for i in range(n+1)])

plt.figure()
plt.plot(t, eta)
plt.xlabel('$t$ [$s$]')
plt.ylabel('$\eta$ [$m$]')

v = np.array([(eta[i+1]-eta[i-1])/(2*h) for i in range(1, n)])

plt.figure()
plt.plot(t[1:n],v)
plt.xlabel('$t$ [$s$]')
plt.ylabel('$v$ [$m/s$]')

a = np.array([(eta[i+1]-2*eta[i]+eta[i-1])/(h**2) for i in range(1, n)])

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


plt.figure()
plt.plot(t,eta,label='$\eta$')
plt.plot(t,eta_1,label='$\eta^{(1)}$')
plt.plot(t,eta_10,label='$\eta^{(10)}$')
plt.plot(t,eta_100,label='$\eta^{(100)}$')
plt.xlabel('$t$ [$s$]')
plt.ylabel('$\eta$ [$m$]')
plt.legend()

plt.figure()
plt.plot(t[1:n],v,label='$v$')
plt.plot(t[1:n],v_1,label='$v^{(1)}$')
plt.plot(t[1:n],v_10,label='$v^{(10)}$')
plt.plot(t[1:n],v_100,label='$v^{(100)}$')
plt.xlabel('$t$ [$s$]')
plt.ylabel('$v$ [$m/s$]')
plt.legend()

plt.figure()
plt.plot(t[1:n],a,label='$a$')
plt.plot(t[1:n],a_1,label='$a^{(1)}$')
plt.plot(t[1:n],a_10,label='$a^{(10)}$')
plt.plot(t[1:n],a_100,label='$a^{(100)}$')
plt.xlabel('$t$ [$s$]')
plt.ylabel('$a$ [$m/s^2$]')
plt.legend()
