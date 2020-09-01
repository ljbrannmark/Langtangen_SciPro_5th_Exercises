# -*- coding: utf-8 -*-
"""
Created on Mon Apr 27 23:06:42 2020

@author: lars-johan.brannmark
"""

def read_constants(filename):
    with open(filename,'r') as infile:
        return {' '.join(row[:-2]): float(row[-2]) for row in 
                [line.split() for line in infile.readlines()[2:]]}

constants = read_constants('constants.txt')