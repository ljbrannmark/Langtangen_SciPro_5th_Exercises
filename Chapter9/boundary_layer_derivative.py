# -*- coding: utf-8 -*-
"""
Created on Sun Sep 13 22:04:14 2020

@author: lars-johan.brannmark
"""

def table(f, x, h_values, methods, dfdx=None):
    """
    Write a table of f'(x) computed numerically by
    the methods in the methods list (class names).
    Each row in the table corresponds to a value of
    the discretization parameter h (in h_values).
    If dfdx is not None, dfdx is the exact derivative
    (a function) and the entries in the table are
    the errors in the numerical approximations.
    """
    # Print headline (h and class names for the methods)
    print '    h      ',
    for method in methods:
        print '%-10s' % method.__name__,
    print  # newline
    # Print table
    for h in h_values:
        print '%10.3E' % h,
        for method in methods:
            if dfdx is not None:
                d = method(f, h, dfdx)
                output = d.error(x)
            else:
                d = method(f, h)
                output = d(x)
            print '%10.3E' % output,
        print  # newline
    print

# =============================================================================
# Plot the function v(x) for mu = 1.0 and mu=0.01
# =============================================================================
import matplotlib.pyplot as plt
import numpy as np

def v(x, mu):
    mu = float(mu)
    return (1-np.exp(x/mu))/(1-np.exp(1/mu))

def dvdx(x, mu):
    mu = float(mu)
    return (-1/mu)*np.exp(x/mu)/(1-np.exp(1/mu))

#Plot v(x, mu) for mu=1.0 and mu=0.01
plt.figure()
x = np.linspace(0, 1, 1001)
mu=1.0
plt.plot(x, v(x, mu), label='$\mu=%g$'%mu)
mu=0.01
plt.plot(x, v(x, mu), label='$\mu=%g$'%mu)
plt.legend()


from Diff2 import *

#Print the table of errors for mu=1.0, 0.01 and x=0.0, 0.9
for mu in [1.0, 0.01]:
    for x in [0.0, 0.9]:
        print '%s\nmu = %.3f, x = %.3f:\n%s'%('-'*22, mu, x, '-'*22)
        table(f=lambda x: v(x, mu),
              x=x,
              h_values=[2**(-k) for k in range(10)],
              methods=[Backward1, Forward1, Forward3, Central2, Central4, Central6],
              dfdx=lambda x: dvdx(x, mu))
