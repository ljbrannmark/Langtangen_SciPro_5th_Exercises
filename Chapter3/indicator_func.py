# -*- coding: utf-8 -*-
"""
Created on Fri Sep 13 16:33:19 2019

@author: larsjohan
"""

def H(x):
    if x < 0:
        return 0
    if x >= 0:
        return 1

def I1(x, L, R):
    if L <= x <= R:
        return 1
    else:
        return 0
    
def I2(x, L, R):
    return H(x-L)*H(R-x)

def test_I1_I2():
    L = -5
    R = 2
    X = [L-10, L-1, L, (L+R)/2.0, R, R+1, R+10] #List of x values
    I = [0, 0, 1, 1, 1, 0, 0]               #List of correct function values 
    success = True
    for i in range(len(X)):
        i1 = I1(X[i], L, R)
        i2 = I2(X[i], L, R)
        success = success & ( i1==I[i] ) & ( i1==i2 )
    msg = "Test of functions I1 and I2 failed!"
    assert success, msg
    
test_I1_I2()