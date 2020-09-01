# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:42:19 2020

@author: lars-johan.brannmark
"""

def get_base_counts2(dna):
    counts = {'A': 0, 'T': 0, 'G': 0, 'C': 0}
    for base in dna:
        if counts.has_key(base):
            counts[base] += 1
    return counts

#Alternative approach:
    
from collections import defaultdict
def get_base_counts3(dna):
    counts = defaultdict(lambda: 0)
    for base in dna:
        counts[base] += 1
    return dict(counts)

dna_test = 'ATGCATGCLLLDDDATGC'
print get_base_counts2(dna_test)
print get_base_counts3(dna_test)