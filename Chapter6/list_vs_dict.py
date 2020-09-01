# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:41:19 2020

@author: lars-johan.brannmark
"""

# Dictionary version
t1 = {}
t1[0] = -5
t1[1] = 10.5

#List version, various alternatives:
t2 = []
t2.append(-5)
t2.append(10.5)

t3 = []
t3 += [-5]
t3 += [10.5]

t4 = [0]*2
t4[0] += -5
t4[1] += 10.5