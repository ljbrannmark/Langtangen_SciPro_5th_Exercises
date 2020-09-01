# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:08:15 2019

@author: larsjohan
"""

q=[['a','b','c'],['d','e','f'],['g','h']]

print q[0][0]
print q[1]
print q[-1][-1]

for i in q:
    for j in range(len(i)):
        print i[j]
