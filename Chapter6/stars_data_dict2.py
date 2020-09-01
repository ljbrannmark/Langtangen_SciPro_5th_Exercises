# -*- coding: utf-8 -*-
"""
Created on Fri May  1 22:37:49 2020

@author: lars-johan.brannmark
"""

filename = 'stars.txt'
with open(filename,'r') as infile:
    exec(infile.read())

d = {star[0]:
    {
     'distance': star[1],
     'apparent brightness': star[2],
     'luminosity': star[3] }
    for star in data
    }

from pprint import pprint
pprint(d)