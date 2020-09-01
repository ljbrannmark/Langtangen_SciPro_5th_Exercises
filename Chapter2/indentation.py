# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:25:52 2019

@author: larsjohan
"""

C = -60; dC = 2
while C <= 60:
    F = (9.0/5)*C + 32
    print C, F
    C = C + dC