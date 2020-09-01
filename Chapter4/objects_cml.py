# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:40:08 2019

@author: lars-johan.brannmark
"""

import sys

r_val = eval(sys.argv[1])
r_type = type(r_val)

print r_type
print 'Value: ', r_val