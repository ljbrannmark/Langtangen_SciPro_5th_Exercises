# -*- coding: utf-8 -*-
"""
Created on Sat May 16 22:43:16 2020

@author: lars-johan.brannmark
"""

from collections import defaultdict

#------------------------------------------------------------------------------
#Define the three distinct types of find_consensus_v* functions:

#List of lists v2
def find_consensus_v2(frequency_matrix):
    if isinstance(frequency_matrix, list) and \
       isinstance(frequency_matrix[0], list):
        pass # right type
    else:
        raise TypeError('frequency_matrix must be list of lists')

    base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    consensus = ''
    dna_length = len(frequency_matrix[0])

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ACGT':
            if frequency_matrix[base2index[base]][i] > max_freq:
                max_freq = frequency_matrix[base2index[base]][i]
                max_freq_base = base
            elif frequency_matrix[base2index[base]][i] == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus

#Dict of dicts v1
def find_consensus_v3(frequency_matrix):
    if isinstance(frequency_matrix, dict) and \
       isinstance(frequency_matrix['A'], dict):
        pass # right type
    else:
        raise TypeError('frequency_matrix must be dict of dicts')

    consensus = ''
    dna_length = len(frequency_matrix['A'])

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ACGT':
            if frequency_matrix[base][i] > max_freq:
                max_freq = frequency_matrix[base][i]
                max_freq_base = base
            elif frequency_matrix[base][i] == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus

#Dict of dicts if default dictionary is used
def find_consensus_v4(frequency_matrix, dna_length):
    if isinstance(frequency_matrix, dict) and \
       isinstance(frequency_matrix['A'], dict):
        pass # right type
    else:
        raise TypeError('frequency_matrix must be dict of dicts')

    consensus = ''

    for i in range(dna_length):  # loop over positions in string
        max_freq = -1            # holds the max freq. for this i
        max_freq_base = None     # holds the corresponding base

        for base in 'ACGT':
            if frequency_matrix[base][i] > max_freq:
                max_freq = frequency_matrix[base][i]
                max_freq_base = base
            elif frequency_matrix[base][i] == max_freq:
                max_freq_base = '-' # more than one base as max

        consensus += max_freq_base  # add new base with max freq
    return consensus

#------------------------------------------------------------------------------
#Define the corresponding functions for creating three distinct types of 
#frequency matrices

def freq_list_of_lists_v2(dna_list):
    frequency_matrix = [[0 for v in dna_list[0]] for x in 'ACGT']
    base2index = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base2index[base]][index] += 1

    return frequency_matrix

#Using bases as keys and dictionaries as values
def freq_dict_of_dicts_v1(dna_list):
    n = max([len(dna) for dna in dna_list])
    frequency_matrix = {base: {index: 0 for index in range(n)}
                        for base in 'ACGT'}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base][index] += 1

    return frequency_matrix

#Using bases as keys and default dictionaries as values
def freq_dict_of_dicts_v2(dna_list):
    n = max([len(dna) for dna in dna_list])
    frequency_matrix = {base: defaultdict(lambda: 0)
                        for base in 'ACGT'}
    for dna in dna_list:
        for index, base in enumerate(dna):
            frequency_matrix[base][index] += 1

    return frequency_matrix

#------------------------------------------------------------------------------
#Define a find_consensus function that can handle all three data structures
    
def find_consensus(frequency_matrix, dna_length=False):
    if isinstance(frequency_matrix,list) and \
    isinstance(frequency_matrix[0],list):
        return find_consensus_v2(frequency_matrix)
    elif isinstance(frequency_matrix,dict) and \
    isinstance(frequency_matrix[frequency_matrix.keys()[0]],dict) and \
    not dna_length:
        return find_consensus_v3(frequency_matrix)
    elif isinstance(frequency_matrix,dict) and \
    isinstance(frequency_matrix[frequency_matrix.keys()[0]],defaultdict) and \
    dna_length>0:
        return find_consensus_v4(frequency_matrix,dna_length)

#------------------------------------------------------------------------------
dna_list = ['ATCGGATGACTGATAGTGATCGTAA',
            'GCCGTAGCTAGTCGATGCATGACGG',
            'ACTGATGTCGTAGCTACATGCGATG',
            'TTGCTGATCGTCAGTAGTACTGAGT',
            'TAAATAATCGTCAGTAGTACTGAGT',
            'TTCATCCTCGTCAGTAGTACTGAGT']

dna_length = len(dna_list[0])

frequency_matrix_1 = freq_list_of_lists_v2(dna_list)
frequency_matrix_2 = freq_dict_of_dicts_v1(dna_list)
frequency_matrix_3 = freq_dict_of_dicts_v2(dna_list)

#------------------------------------------------------------------------------
print find_consensus(frequency_matrix_1)
print find_consensus(frequency_matrix_2)
print find_consensus(frequency_matrix_3, dna_length)



