# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 23:37:17 2019

@author: larsjohan
"""

n=10

v0=20.0
g=9.81

a=0.0
b=2*v0/g

h=float(b-a)/n

T=[a + i*h for i in range(n+1)]
Y=[v0*t - 1.0/2*g*t**2 for t in T ]
    
ty1=[T , Y]
ty2=[[t,y] for t,y in zip(T,Y)]

for i in range(n+1):
    for j in range(2):
        print '%6.2f' %(ty1[j][i]),
    print
    
print '---------------------'

for i in range(n+1):
    for j in range(2):
        print '%6.2f' %(ty2[i][j]),
    print

print '---------------------'
        
