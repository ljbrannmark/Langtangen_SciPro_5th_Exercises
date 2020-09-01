# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:39:55 2020

@author: lars-johan.brannmark
"""

from numpy import *
import matplotlib.pyplot as plt
import sys


try:
    f_str = sys.argv[1]
    xmin = float(eval(sys.argv[2]))
    xmax = float(eval(sys.argv[3]))
except IndexError:
    print 'Too few input arguments given'
    sys.exit(1)
except Exception as e:
    print e
    sys.exit(1)
    
if len(sys.argv) > 4:
    try:
        n = int(eval(sys.argv[4]))
        if n <= 0:
            raise ValueError('Number of points n must be a positive integer, not %s' %sys.argv[4])
    except Exception as e:
        print e
        sys.exit(1)
else:
    n = 501
    
try:
    x = linspace(xmin, xmax, n)
    y = zeros_like(x)
    y[:] = eval(f_str)
except Exception as e:
    print e
    sys.exit(1)
    
plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('tmp.png')
plt.show()