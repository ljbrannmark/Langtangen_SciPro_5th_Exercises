# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 23:07:51 2020

@author: lars-johan.brannmark
"""

from numpy import *
import matplotlib.pyplot as plt
import sys

x = linspace(eval(sys.argv[2]), eval(sys.argv[3]), 501)
plt.plot(x, eval(sys.argv[1]))
plt.xlabel('x')
plt.ylabel('y')
plt.savefig('tmp.png')
plt.show()