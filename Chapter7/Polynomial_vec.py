# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:11:32 2020

@author: lars-johan.brannmark
"""

import numpy as np

class Polynomial(object):
    def __init__(self, coefficients):
        self.coeff = np.array(coefficients, dtype=float)

    def __call__(self, x):
        """Evaluate the polynomial."""
        return np.dot(self.coeff, x**np.arange(len(self.coeff)))

    def __add__(self, other):
        """Return self + other as Polynomial object."""
        # Two cases:
        #
        # self:   X X X X X X X
        # other:  X X X
        #
        # or:
        #
        # self:   X X X X X
        # other:  X X X X X X X X

        # Start with the longest list and add in the other
        s_len = len(self.coeff)
        o_len = len(other.coeff)
        if s_len > o_len:
            result_coeff = np.concatenate( (self.coeff[0:o_len] + other.coeff,\
                                            self.coeff[o_len:]) )
        else:
            result_coeff = np.concatenate( (self.coeff + other.coeff[0:s_len],\
                                            other.coeff[s_len:]) )
        return Polynomial(result_coeff)
    
    def __sub__(self, other):
        return self + Polynomial([-c for c in other.coeff])

    def __mul__(self, other):
        return Polynomial(np.convolve(self.coeff, other.coeff))

    def differentiate(self):
        """Differentiate this polynomial in-place."""
        n = len(self.coeff)
        self.coeff[:-1] = np.linspace(1, n-1, n-1)*self.coeff[1:]
        self.coeff = self.coeff[:-1]

    def derivative(self):
        """Copy this polynomial and return its derivative."""
        dpdx = Polynomial(self.coeff[:])  # make a copy
        dpdx.differentiate()
        return dpdx

    def __str__(self):
        s = ''
        for i in range(0, len(self.coeff)):
            if self.coeff[i] != 0:
                s += ' + %g*x^%d' % (self.coeff[i], i)
        # Fix layout
        s = s.replace('+ -', '- ')
        s = s.replace('x^0', '1')
        s = s.replace(' 1*', ' ')
        s = s.replace('x^1 ', 'x ')
        #s = s.replace('x^1', 'x') # will replace x^100 by x^00
        if s[0:3] == ' + ':  # remove initial +
            s = s[3:]
        if s[0:3] == ' - ':  # fix spaces for initial -
            s = '-' + s[3:]
        return s

    def simplestr(self):
        s = ''
        for i in range(0, len(self.coeff)):
            s += ' + %g*x^%d' % (self.coeff[i], i)
        return s


def test_Polynomial():
    p1 = Polynomial([1, -1])
    p2 = Polynomial([0, 1, 0, 0, -6, -1])
    p3 = p1 + p2
    p3_exact = Polynomial([1, 0, 0, 0, -6, -1])
    msg = 'p1 = %s, p2 = %s\np3=p1+p2 = %s\nbut wrong p3 = %s'%\
          (p1, p2, p3_exact, p3)
    assert (p3.coeff == p3_exact.coeff).all(), msg
    # Note __add__ applies lists only, here with integers, so
    # == for comparing lists is not subject to round-off errors
    
    msg = 'Error in function Polynomial__call__'
    assert p1(2) == -1.0, msg

    p4 = p1*p2
    # p4.coeff becomes a numpy array, see __mul__
    p4_exact = Polynomial(np.array([0.,  1., -1.,  0., -6.,  5.,  1.]))
    msg = 'p1 = %s, p2 = %s\np4=p1*p2 = %s\ngot wrong p4 = %s'%\
          (p1, p2, p4_exact, p4)
    assert np.allclose(p4.coeff, p4_exact.coeff, rtol=1E-14), msg

    p5 = p2.derivative()
    p5_exact = Polynomial([1, 0, 0, -24, -5])
    msg = 'p2 = %s\np5 = p2.derivative() = %s\ngot wrong p5 = %s'%\
          (p2, p5_exact, p5)
    assert (p5.coeff == p5_exact.coeff).all(), msg

    p6 = Polynomial([0, 1, 0, 0, -6, -1])  # p2
    p6.differentiate()
    p6_exact = p5_exact
    msg = 'p6 = %s\p6.differentiate() = %s\ngot wrong p6 = %s'%\
          (p2, p6_exact, p6)
    assert (p6.coeff == p6_exact.coeff).all(), msg
    
    p7 = Polynomial([1, -1])
    p8 = Polynomial([0, 1, 0, 0, -6, -1])
    p9 = p7 - p8
    p9_exact = Polynomial([1, -2, 0, 0, 6, 1])
    msg = 'p7 = %s, p8 = %s\np9=p7+p8 = %s\nbut wrong p9 = %s'%\
          (p7, p8, p9_exact, p9)
    assert (p9.coeff == p9_exact.coeff).all, msg    
    
test_Polynomial()
