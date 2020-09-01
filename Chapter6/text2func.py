# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:26:33 2020

@author: lars-johan.brannmark
"""

import sys
from scitools.StringFunction import StringFunction
from math import pi, sin, cos, exp, sqrt

def text2function(str_in):
    str_in_1 = str_in.split(' is a function of ')
    str_in_2 = str_in_1[1].split(' with parameter ')
    
    f_expr = str_in_1[0]
    indvar = "'" + str_in_2[0].replace(" ","").replace(",","','") + "'"
    if len(str_in_2) > 1:
        param = ', ' + str_in_2[1]
    else:
        param = ''
    
    inputstr = "StringFunction(f_expr, independent_variables=[%s]%s)" %(indvar,param)
    print inputstr
    f = eval(inputstr)
    return f


f = text2function(' '.join(sys.argv[1:]))


def test_text2function():
    tol = 1e-12
    old_sys_argv = sys.argv
    
    # Test with arguments as given on the command line without quotes
    sys.argv = [old_sys_argv[0]] + ['sin(x)', 'is', 'a', 'function', 'of', 'x']
    f = text2function(' '.join(sys.argv[1:]))
    x = pi/4;
    f_exact = sin(x)
    f_comp = f(x)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    sys.argv = [old_sys_argv[0]] + ['sin(a*y)', 'is', 'a', 'function', 'of', 'y', 'with', 'parameter', 'a=2']
    f = text2function(' '.join(sys.argv[1:]))
    y = pi/8;
    a = 2;
    f_exact = sin(a*y)
    f_comp = f(y)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    sys.argv = [old_sys_argv[0]] + ['sin(a*x-phi)', 'is', 'a', 'function', 'of', 'x', 'with', 'parameter', 'a=3,', 'phi=-pi']
    f = text2function(' '.join(sys.argv[1:]))
    a = 3
    phi = -pi
    x = 0.25
    f_exact = sin(a*x-phi)
    f_comp = f(x)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    sys.argv = [old_sys_argv[0]] + ['exp(-a*x)*cos(w*t)', 'is', 'a', 'function', 'of', 't', 'with', 'parameter', 'a=1,', 'w=pi,', 'x=2']
    f = text2function(' '.join(sys.argv[1:]))
    a = 1
    w = pi
    x = 2
    t = 2.0
    f_exact = exp(-a*x)*cos(w*t)
    f_comp = f(t)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    sys.argv = [old_sys_argv[0]] + ['exp(-a*x*y)*cos(w*t)', 'is', 'a', 'function', 'of', 'x,', 'y,', 't', 'with', 'parameter', 'a=1,', 'w=pi']
    f = text2function(' '.join(sys.argv[1:]))
    a = 1
    w = pi
    x = 2.0
    y = 1.5
    t = 0.8
    f_exact = exp(-a*x*y)*cos(w*t)
    f_comp = f(x,y,t)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    ##### Now test with arguments given as a single string
    
    sys.argv = [old_sys_argv[0]] + ["sin(x) is a function of x"]
    f = text2function(' '.join(sys.argv[1:]))
    x = pi/4;
    f_exact = sin(x)
    f_comp = f(x)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    sys.argv = [old_sys_argv[0]] + ["sin(a*y) is a function of y with parameter a=2"]
    f = text2function(' '.join(sys.argv[1:]))
    y = pi/8;
    a = 2;
    f_exact = sin(a*y)
    f_comp = f(y)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    sys.argv = [old_sys_argv[0]] + ["sin(a*x-phi) is a function of x with parameter a=3, phi=-pi"]
    f = text2function(' '.join(sys.argv[1:]))
    a = 3
    phi = -pi
    x = 0.25
    f_exact = sin(a*x-phi)
    f_comp = f(x)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    sys.argv = [old_sys_argv[0]] + ["exp(-a*x)*cos(w*t) is a function of t with parameter a=1, w=pi, x=2"]
    f = text2function(' '.join(sys.argv[1:]))
    a = 1
    w = pi
    x = 2
    t = 2.0
    f_exact = exp(-a*x)*cos(w*t)
    f_comp = f(t)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg
    
    sys.argv = [old_sys_argv[0]] + ["exp(-a*x*y)*cos(w*t) is a function of x, y, t with parameter a=1, w=pi"]
    f = text2function(' '.join(sys.argv[1:]))
    a = 1
    w = pi
    x = 2.0
    y = 1.5
    t = 0.8
    f_exact = exp(-a*x*y)*cos(w*t)
    f_comp = f(x,y,t)
    msg = 'Test fail!'
    print f_exact, f_comp
    success = abs(f_exact - f_comp) < tol
    assert success, msg

    sys.argv = old_sys_argv

test_text2function()

