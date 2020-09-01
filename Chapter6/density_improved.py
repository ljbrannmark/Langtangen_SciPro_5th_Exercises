# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:52:06 2020

@author: lars-johan.brannmark
"""

def read_densities_v1(filename):
    infile = open(filename, 'r')
    densities = {}
    for line in infile:
        words = line.split()
        density = float(words[-1])

        if len(words[:-1]) == 2:
            substance = words[0] + ' ' + words[1]
        else:
            substance = words[0]

        densities[substance] = density
    infile.close()
    return densities

def read_densities_v2(filename):
    with open(filename, 'r') as infile:
        return {' '.join(words[:-1]): float(words[-1]) for words in 
                [line.split() for line in infile.readlines()]}

def read_densities_v3(filename):
    with open(filename, 'r') as infile:
        return {substance.strip(): float(density) for substance, density in
                [(line[:12], line[12:]) for line in infile.readlines()]}

densities_1 = read_densities_v1('densities.dat')
densities_2 = read_densities_v2('densities.dat')
densities_3 = read_densities_v3('densities.dat')

def test_densities():
    densities_1 = read_densities_v1('densities.dat')
    densities_2 = read_densities_v2('densities.dat')
    densities_3 = read_densities_v3('densities.dat')
    success = densities_1 == densities_2 and densities_2 == densities_3
    msg = 'Functions do not produce same result!'
    assert success, msg
    
from scitools.pprint2 import pprint
pprint(densities_1)
print
pprint(densities_2)
print
pprint(densities_3)

test_densities()


