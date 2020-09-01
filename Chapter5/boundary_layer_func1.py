# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 22:40:51 2020

@author: lars-johan.brannmark
"""

import numpy as np
import math
import matplotlib.pyplot as plt

#########################################################################
# Exercise 5.51 a)
def v(x, mu=1E-6, exp=math.exp):
    try:
        num = 1.0 - exp(x/mu)
        den = 1.0 - exp(1.0/mu)
        v = num/den
    except:
        v = np.NaN
        try:
            num = 1.0 - exp(x/mu)
        except:
            num = np.NaN
        try:
            den = 1.0 - exp(1.0/mu)
        except:
            den = np.NaN       
    return v, num, den

#########################################################################
# Exercise 5.51 b)
mu = 1E-3
x_values = np.linspace(0, 1, 10)
exp_list = [math.exp, np.exp]

print 'Exercise 5.51 b):\n'
print 'x           | Function                 |             v(x) |            num  |            den'
print '--------------------------------------------------------------------------------------------'
for x in x_values:
    for exp in exp_list:
        val, num, den = v(x, mu, exp)
        print '%-10.2g  | %-25s: %15.5g  |%15.5g  |%15.5g'%(x, exp.__str__(), val, num, den)
    print '-'*(18*3+25+10+3)

#########################################################################
# Exercise 5.51 c)
mu_values = [1.0, 0.1, 0.01, 0.001]
x = np.linspace(0, 1, 10000)
plt.figure()
for mu in mu_values:
    val, num, den = v(x, mu, np.exp)
    plt.plot(x, val, label='mu=%.4g'%mu)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

#########################################################################
# Exercise 5.51 d)
mu = 1E-3
x_values = np.linspace(0, 1, 10)
exp_list = [math.exp, np.exp]
print '\n\n'
print 'Exercise 5.51 d): Repeat Exercise 5.51 b) using np.longdouble() for x and mu:\n'
print 'x           | Function                 |             v(x) |            num  |            den'
print '--------------------------------------------------------------------------------------------'
for x in x_values:
    for exp in exp_list:
        val, num, den = v(np.longdouble(x), np.longdouble(mu), exp)
        print '%-10.2g  | %-25s: %15.5g  |%15.5g  |%15.5g'%(x, exp.__str__(), val, num, den)
    print '-'*(18*3+25+10+3)

#########################################################################
# Exercise 5.51 e)
mu = 1E-3
x_values = np.linspace(0, 1, 10)
exp_list = [math.exp, np.exp]
print '\n\n'
print 'Exercise 5.51 e): Repeat Exercise 5.51 b) using np.float32() for x and mu:\n'
print 'x           | Function                 |             v(x) |            num  |            den'
print '--------------------------------------------------------------------------------------------'
for x in x_values:
    for exp in exp_list:
        val, num, den = v(np.float32(x), np.float32(mu), exp)
        print '%-10.2g  | %-25s: %15.5g  |%15.5g  |%15.5g'%(x, exp.__str__(), val, num, den)
    print '-'*(18*3+25+10+3)
    
    