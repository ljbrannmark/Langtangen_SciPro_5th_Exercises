# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 22:17:49 2019

@author: lars-johan.brannmark
"""

def halve(x):
    return x/2

def test_halve():
    assert halve(5.0) == 2.5  # Real nomber division
    assert halve(5) == 2      # Integer division
    
def add(a, b):
    return a + b

def test_add():
    # Test integers
    assert add(1, 2) == 3
    
    # Test floating-point numbers with rounding error
    tol = 1E-14
    a = 0.1; b = 0.2
    computed = add(a, b)
    expected = 0.3
    assert abs(expected - computed) < tol
    
    # Test lists
    assert add([1,4], [4,7]) == [1,4,4,7]
    
    # Test strings
    assert add('Hello, ', 'World!') == 'Hello, World!'
    
def equal(s1, s2):
    eq = s1 == s2
    s1 += '*' * (len(s2) - len(s1))
    s2 += '*' * (len(s1) - len(s2))
    outstr = ''
    for a, b in zip(s1,s2):
        outstr += a if a==b else a + '|' + b
    return eq, outstr
            
    
def test_equal():
    assert equal('abc', 'abc') == (True, 'abc')
    assert equal('abc', 'aBc') == (False, 'ab|Bc')
    assert equal('abc', 'aBcd') == (False, 'ab|Bc*|d')
    assert equal('Hello, World!', 'hello world') == \
                (False, 'H|hello,|  |wW|oo|rr|ll|dd|*!|*')