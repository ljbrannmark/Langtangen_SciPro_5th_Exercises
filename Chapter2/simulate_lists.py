# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 09:39:38 2019

@author: larsjohan
"""

a = [1,3,5,7,11]
b = [13,17]
c = a + b
print c
b[0]=-1
d=[e+1 for e in a]
print d
d.append(b[0] + 1)
d.append(b[-1] + 1)
print d[-2:]
for e1 in a:
    for e2 in b:
        print e1 + e2
