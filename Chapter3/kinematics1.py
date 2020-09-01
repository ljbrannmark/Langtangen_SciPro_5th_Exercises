# -*- coding: utf-8 -*-
"""
Created on Mon Sep  9 22:31:33 2019

@author: larsjohan
"""

def kinematics(i, x, t):
    v_i = ( x[i+1] - x[i-1] ) / float( t[i+1] - t[i-1] )
    a_i = 2*( t[i+1] - t[i-1] )**-1 * ( ( x[i+1] - x[i] ) / float( t[i+1] - t[i] ) \
             - ( x[i] - x[i-1] ) / float( t[i] - t[i-1] ) )
    return v_i, a_i

def test_kinematics():
    V = 5.0
    t = [0, 0.5, 1.5, 2.2]
    x = []
    for ti in t:
           x.append(V*ti)
    for i in range(1,len(t)-1):
        v_expected = V
        a_expected = 0.0
        v_i, a_i = kinematics(i, x, t)
        success = ( abs(v_i - v_expected) < 1E-12 ) & ( abs(a_i - a_expected) < 1E-12 )
        msg = 'Function kinematics failed'
        assert success, msg

test_kinematics()
