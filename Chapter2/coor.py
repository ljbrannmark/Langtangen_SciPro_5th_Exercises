# -*- coding: utf-8 -*-
"""
Created on Fri Mar 01 15:23:21 2019

@author: larsjohan
"""

n=10
a=2.0
b=5.0

h = float(b-a) / n

#Create n+1 equally spaced coordinates in [a,b], using a for loop
x1 = []
for i in range(n+1):
    x1.append(a+i*h)
    
print x1

#Create n+1 equally spaced coordinates in [a,b], using list comprehension
x2 = [a+i*h for i in range(n+1)]

print x2