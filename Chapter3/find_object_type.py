# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 22:07:50 2019

@author: larsjohan
"""

def makelist(start, stop, inc):
    value = start
    result = []
    while value <= stop:
        result.append(value)
        value = value + inc
    return result

#l1 = makelist(0, 100, 1)
#l2 = makelist(0, 100, 1.0)
#l3 = makelist(-1, 1, 0.1)
#l4 = makelist(10, 20, 20)
#l5 = makelist([1,2], [3,4], [5])
#l6 = makelist((1,-1,1), ('myfile.dat', 'yourfile.dat'))
#l7  = makelist('myfile.dat', 'yourfile.dat', 'herfile.dat')
