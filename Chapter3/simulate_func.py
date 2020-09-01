# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 16:35:02 2019

@author: larsjohan
"""

def a(x):
    q = 2
    x = 3*x
    return q + x

def b(x):
    global q
    q += x
    return q + x

q=0
x=3

print a(x), b(x), a(x), b(x)