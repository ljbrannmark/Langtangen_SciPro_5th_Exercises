# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 21:57:54 2020

@author: lars-johan.brannmark
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 23:11:32 2020

@author: lars-johan.brannmark
"""

import numpy as np

class Polynomial(object):
    def __init__(self, coeff_dict):
        self.coeff = coeff_dict

    def __call__(self, x):
        """Evaluate the polynomial."""
        return sum([c*x**p for p, c in self.coeff.iteritems()])

    def __add__(self, other):
        """Return self + other as Polynomial object."""
        result = self.coeff.copy()
        for p in other.coeff:
            if p in result:
                result[p] += other.coeff[p]
            else:
                result[p] = other.coeff[p]
        return Polynomial(result)
        
    def __sub__(self, other):
        return self + Polynomial({p: -c for p, c in other.coeff.iteritems()})

    def __mul__(self, other):
        c = self.coeff
        d = other.coeff
        result = {}
        for i in c.keys():
            for j in d.keys():
                if i+j in result:
                    result[i+j] += c[i]*d[j]
                else:
                    result[i+j] = c[i]*d[j]
        return Polynomial(result)

def test_Polynomial():
        p1 = Polynomial({4: 1, 2: -2, 0: 3})
        x = 2.0
        p1_exact = 11.0
        success = abs(p1(x) - p1_exact) < 1e-12
        msg = 'Error in Polynomial.__call__'
        assert success, msg
        
        p1 = Polynomial({4: 1, 2: -2, 0: 3})
        p2 = Polynomial({0: 4, 1: 3})
        p3 = p1 + p2
        p3_exact = Polynomial({0: 7, 1: 3, 2: -2, 4: 1})
        s1 = set(p3.coeff.items())
        s2 = set(p3_exact.coeff.items())
        success = set.symmetric_difference(s1, s2) == set()
        msg = 'Error in Polyomial.__add__'
        assert success, msg
        
        p1 = Polynomial({0: 1, 3: 1})
        p2 = Polynomial({1: -2, 2: 3})
        p3 = p1*p2
        p3_exact = Polynomial({1: -2, 2: 3, 4: -2, 5: 3})
        s1 = set(p3.coeff.items())
        s2 = set(p3_exact.coeff.items())
        success = set.symmetric_difference(s1, s2) == set()
        msg = 'Error in Polyomial.__mul__'
        assert success, msg
        
test_Polynomial()
