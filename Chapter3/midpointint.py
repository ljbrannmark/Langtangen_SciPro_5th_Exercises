# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 21:51:48 2019

@author: larsjohan
"""

from math import pi, sin, cos

def midpointint(f, a, b, n):
    h = float(b-a)/n
    s = 0.0
    for i in range(n):
        s += f(a + i*h + 0.5*h)
    return h*s

I0_exact = 0
I1_exact = 2
I2_exact = 1

I0 = midpointint(cos, 0, pi ,10)
I1 = midpointint(sin, 0, pi, 10)
I2 = midpointint(sin, 0, pi/2, 10)
e0 = I0_exact - I0
e1 = I1_exact - I1
e2 = I2_exact - I2