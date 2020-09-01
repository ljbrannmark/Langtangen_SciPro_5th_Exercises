# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 22:24:12 2019

@author: larsjohan
"""

def max(x):
    max_elem=x[0]
    for x_i in x[1:]:
        if x_i > max_elem:
            max_elem = x_i
    return max_elem

def min(x):
    min_elem=x[0]
    for x_i in x[1:]:
        if x_i < min_elem:
            min_elem = x_i
    return min_elem

