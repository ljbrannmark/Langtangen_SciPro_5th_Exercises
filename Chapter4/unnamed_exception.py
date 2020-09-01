# -*- coding: utf-8 -*-
"""
Created on Sat Dec  7 22:01:42 2019

@author: lars-johan.brannmark
"""
import sys
try:
    C = float(sys.argv[1])
except IndexError:
    print 'C must be provided as command-line argument'
    sys.exit(1)
except ValueError:
    print 'C must be a pure number'
    sys.exit(1)