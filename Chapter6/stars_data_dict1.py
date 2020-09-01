# -*- coding: utf-8 -*-
"""
Created on Fri May  1 21:46:27 2020

@author: lars-johan.brannmark
"""

filename = 'stars.txt'
with open(filename,'r') as infile:
    exec(infile.read())

d = {star[0]: star[-1] for star in data}