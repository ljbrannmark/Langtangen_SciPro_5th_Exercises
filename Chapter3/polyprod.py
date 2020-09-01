# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 15:25:20 2019

@author: larsjohan
"""

def poly(x,roots):
    p=1;
    for i in range(len(roots)):
        p=p*(x-roots[i])
    return p
        
def test_poly():
    x1=3
    exact1=-12
    computed1=poly(x1,[1,2,4,5,6])
    
    x2=8.0
    exact2=50.0
    computed2=poly(x2,[1.0+1.0j,1.0-1.0j])
    
    success = exact1==computed1 and exact2==computed2
    msg='Function poly() failed test'
    assert success, msg
     
test_poly()
