# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 22:56:46 2020

@author: lars-johan.brannmark
"""

import math
import numpy as np

class Vec(object):
    def __init__(self, *args):
        if len(args) == 1:
            self.v = np.asarray(args[0], dtype=float)
        else:
            self.v = np.array(args, dtype=float)

    def __add__(self, other):
        return Vec(self.v + other.v)

    def __sub__(self, other):
        return Vec(self.v - other.v)

    def __mul__(self, other):
        return np.dot(self.v, other.v)

    def __eq__(self, other):
        return (self.v == other.v).all()

    def __str__(self):
        return str(self.v)

    def __abs__(self):
        return math.sqrt(np.dot(self.v, self.v))

    def __ne__(self, other):
        return not self.__eq__(other)  # reuse __eq__
