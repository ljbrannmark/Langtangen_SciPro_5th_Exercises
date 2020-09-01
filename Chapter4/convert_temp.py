# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:12:29 2019

@author: lars-johan.brannmark

A module for converting temeratures between Celsius, Fahrenheit and Kelvin.
Usage
-----
In [1]: C2F(20)
Out[1]: 68.0

In [2]: F2C(68)
Out[2]: 20.0

In [3]: C2K(0)
Out[3]: 273.15

In [4]: K2C(0)
Out[4]: -273.15

In [5]: F2K(32)
Out[5]: 273.15

In [6]: K2F(0)
Out[6]: -459.66999999999996
"""

def C2F(C):
    return 9.0*C/5.0 + 32

def F2C(F):
    return (F-32)*5.0/9.0

def C2K(C):
    return C + 273.15

def K2C(K):
    return K - 273.15

def F2K(F):
    return C2K(F2C(F))

def K2F(K):
    return C2F(K2C(K))

def test_conversion():
    success = True
    tol = 1E-12
    if abs(C2F(F2C(10)) - 10) > tol:
        success = False
    if abs(K2C(C2K(10)) - 10) > tol:
        success = False
    if abs(K2F(F2K(10)) - 10) > tol:
        success = False
    msg = 'Verification of module convert_temp failed!'
    assert success, msg
    
def convert(t,scale):
    if scale == 'C':
        print '%.2f°C is %.2f°F and %.2f°K' %(t,C2F(t),C2K(t))
    if scale == 'F':
        print '%.2f°F is %.2f°C and %.2f°K' %(t,F2C(t),F2K(t))
    if scale == 'K':
        print '%.2f°K is %.2f°C and %.2f°F' %(t,K2C(t),K2F(t))
    
if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'verify':
            test_conversion()
            print "Module sucessfully tested"
        else:
            convert(float(sys.argv[1]),sys.argv[2])
    
__all__ = ['C2F','F2C','C2K','K2C','F2K','K2F']

    
    
    
    