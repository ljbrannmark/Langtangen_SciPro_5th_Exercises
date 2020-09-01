# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 22:05:52 2019

@author: lars-johan.brannmark
"""

import sys

try:
    F = float(sys.argv[1])
except IndexError:
    print 'Fahrenheit degrees must be supplied on the command line'
    sys.exit(1) # abort execution
except ValueError:
    print 'Fahrenheit degrees must be given as a pure number, '\
          'not "%s"' % sys.argv[1]
    sys.exit(1)
    
C = (F-32)*5/9.0
print C