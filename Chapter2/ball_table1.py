# -*- coding: utf-8 -*-
"""
Created on Fri Mar 01 16:09:10 2019

@author: larsjohan
"""

n=10

v0=20.0
g=9.81

a=0.0
b=2*v0/g

h=float(b-a)/n
    
table1=[]
for i in range(n+1):
    t=a+i*h
    y=v0*t - 1.0/2*g*t**2
    table1.append([t,y])

table2=[]
t=a
while t <= 2*v0/g + h/100:
    y=v0*t - 1.0/2*g*t**2
    table2.append([t,y])
    t+=h
    

#Some other approaches, using pre-stored values of t, y(t)
    
T=[a + i*h for i in range(n+1)]
Y=[v0*t - 1.0/2*g*t**2 for t in T ]

table3=[]
for t,y in zip(T,Y):
    table3.append([t,y])
    
table4=[]
for i in range(len(T)):
    table4.append([T[i], Y[i]])
    
table5=[]
i=0
while i < len(T):
    table5.append([T[i],Y[i]])
    i+=1