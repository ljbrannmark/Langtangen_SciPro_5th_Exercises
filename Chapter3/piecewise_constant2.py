# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 21:53:05 2019

@author: larsjohan
"""

def I(x, L, R):
    if L <= x < R:
        return 1
    else:
        return 0

def piecewise(x,data):
    n=len(data)-1
    v = 0
    for i in range(n):
        v += data[i][1]*I( x, data[i][0], data[i+1][0])
    if x >= data[n][0]:
        v += data[n][1]
    return v  

def test_piecewise():
    data=[(-3,9), (0,-1), (1,0), (1.5,4), (2,3.44)]
    p1=piecewise(-3.0,data)
    p2=piecewise(-1.1,data)
    p3=piecewise(0.0,data)
    p4=piecewise(0.99,data)
    p5=piecewise(1.0,data)
    p6=piecewise(1.4,data)
    p7=piecewise(1.5,data)
    p8=piecewise(1.9,data)
    p9=piecewise(2.0,data)
    p10=piecewise(10,data)
    success = True
    success = success & ( p1==9 )
    success = success & ( p2==9 )
    success = success & ( p3==-1 )
    success = success & ( p4==-1 )
    success = success & ( p5==0 )
    success = success & ( p6==0 )
    success = success & ( p7==4 )
    success = success & ( p8==4 )
    success = success & ( p9==3.44 )
    success = success & ( p10==3.44 )
 
    msg = 'Function piecewise failed'
    assert success, msg
    
test_piecewise()