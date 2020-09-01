# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 00:10:50 2019

@author: larsjohan
"""

def f(x):
    if 0 <= x <= 2:
        return x**2
    elif 2 < x <= 4:
        return 4
    elif x < 0:
        return 0
