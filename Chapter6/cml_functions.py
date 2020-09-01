# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:08:26 2020

@author: lars-johan.brannmark
"""


#Exercise 6.12 a)
import sys
from scitools.StringFunction import StringFunction
parameters = {}
for prm in sys.argv[4:]:
    key, value = prm.split('=')
    parameters[key] = eval(value)
f = StringFunction(sys.argv[1], independent_variables=sys.argv[2],
                   **parameters)

var = float(sys.argv[3])
print f(var)

#Exercise 6.12 b)
import sys
from scitools.StringFunction import StringFunction
f = eval('StringFunction(sys.argv[1], ' + \
         'independent_variables=sys.argv[2], %s)' % \
         (', '.join(sys.argv[4:])))
var = float(sys.argv[3])
print f(var)

#For example, run this file with command line arguments as follows:
#run cml_functions.py x**2+4*p1+5*p2 x 3 p1=2 p2=4
