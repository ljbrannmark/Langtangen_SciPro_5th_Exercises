# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 16:13:28 2019

@author: larsjohan
"""
from math import pi, sin, cos

def trapezint1(f, a, b):
    return float(b-a)/2 * (f(a)+f(b))

def trapezint2(f, a, b):
    h=float(b-a)/2
    return trapezint1(f,a,a+h) + trapezint1(f,b-h,b)

def trapezint(f, a, b, n):
    h = float(b-a)/n
    s=0.0
    for i in range(1,n):
        xi = a + i*h
        s += f(xi)
    I = 0.5*h*(f(a)+f(b)) + h*s
    return I

I0_exact = 0
I1_exact = 2
I2_exact = 1

I0_1 = trapezint1(cos,0,pi)
I1_1 = trapezint1(sin,0,pi)
I2_1 = trapezint1(sin,0,pi/2)
e0_1 = I0_exact - I0_1
e1_1 = I1_exact - I1_1
e2_1 = I2_exact - I2_1

I0_2 = trapezint2(cos,0,pi)
I1_2 = trapezint2(sin,0,pi)
I2_2 = trapezint2(sin,0,pi/2)
e0_2 = I0_exact - I0_2
e1_2 = I1_exact - I1_2
e2_2 = I2_exact - I2_2

I0_3 = trapezint(cos, 0, pi ,10)
I1_3 = trapezint(sin, 0, pi, 10)
I2_3 = trapezint(sin, 0, pi/2, 10)
e0_3 = I0_exact - I0_3
e1_3 = I1_exact - I1_3
e2_3 = I2_exact - I2_3

def test_trapezint():
    f = lambda x: 4*x - 3
    a = 0
    b = 5
    I_f_exact = 35.0
    I_f_computed = trapezint(f,a,b,100)
    success = abs(I_f_exact - I_f_computed) < 1E-14
    msg = 'Function trapezoid(f,a,b,n) failed test'
    assert success, msg

test_trapezint()
