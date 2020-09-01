# -*- coding: utf-8 -*-
"""
Created on Thu Jul 16 22:34:59 2020

@author: lars-johan.brannmark
"""

from Polynomial import Polynomial

def test_Polynomial_str():
    p1 = Polynomial([0, 2, 0, 4, 0, 6, 0, 8, 0, 10])
    p2 = Polynomial([1.5, 0, 3.4, 0, 5.5, 0, 7.5, 0, 9.5, 0])
    success = str(p1) == '2*x + 4*x^3 + 6*x^5 + 8*x^7 + 10*x^9' \
    and str(p2) == '1.5*1 + 3.4*x^2 + 5.5*x^4 + 7.5*x^6 + 9.5*x^8'
    msg = 'Error in function Polynomial.__str__'
    assert success, msg
    
test_Polynomial_str()