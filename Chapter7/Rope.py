# -*- coding: utf-8 -*-
"""
Created on Sun Jun 28 22:54:37 2020

@author: lars-johan.brannmark
"""

class Rope(object):
    
    def __init__(self, knots):
        self.knots = knots
        
    def __add__(self, other):
        return Rope(self.knots + other.knots + 1)
    
    def __str__(self):
        return '%g' %self.knots
    
def test_Rope():
    rope1 = Rope(2)
    rope2 = Rope(3)
    rope3 = rope1 + rope2
    success = rope3.knots == rope1.knots + rope2.knots + 1
    msg = 'Error in class Rope'
    assert success, msg
        