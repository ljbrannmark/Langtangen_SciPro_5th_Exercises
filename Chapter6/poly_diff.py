# -*- coding: utf-8 -*-
"""
Created on Sat May  9 23:31:30 2020

@author: lars-johan.brannmark
"""

p = {0: -3, 3: 2, 5: -1}

def diff(poly):
    return {j-1: j*poly[j] for j in poly if j != 0}

print diff(p)