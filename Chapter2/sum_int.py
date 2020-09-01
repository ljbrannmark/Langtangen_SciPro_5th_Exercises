# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 16:48:02 2019

@author: larsjohan
"""

n=10

s=0
for i in range(1,n+1):
    s += i
    
s_compare = n*(n+1)/2

print 's=%d , s_compare=%d' %(s,s_compare)