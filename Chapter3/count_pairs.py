# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:22:08 2019

@author: larsjohan
"""

def count_pairs(dna,pair):
    c=0
    for i in range(len(dna)-1):
        if dna[i:i+2]==pair:
            c+=1
    return c