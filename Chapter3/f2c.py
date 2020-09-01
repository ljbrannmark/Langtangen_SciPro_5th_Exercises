# -*- coding: utf-8 -*-
"""
Created on Fri Jun 21 23:55:18 2019

@author: larsjohan
"""
from math import *

def C(F):
    return 5.0/9*(F - 32)

def F(C):
    return 9.0/5*C + 32

c=50
print C(F(c))

f=122
print F(C(f))