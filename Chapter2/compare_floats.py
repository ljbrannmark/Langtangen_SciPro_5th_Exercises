# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:25:29 2019

@author: larsjohan
"""
a = 1/947.0*947
b = 1
if a != b:
    print 'Wrong result!' 
    print '-------------------'
    
tol=10**-15
if abs(a-b) < tol:
    print 'a-b < tol'
else:
    print 'a != b'
        
