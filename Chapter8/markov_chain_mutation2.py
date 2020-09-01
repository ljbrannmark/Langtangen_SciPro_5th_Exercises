# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 16:03:29 2020

@author: lars-johan.brannmark
"""
# This exercise seems a bit flawed..
#
# Functions transition (with variable interval_limits) and 
# mutate_via_markov_chain referred to in Exercise 8.47, seem to refer
# to those in dna_functions.py of Chapter 9. Section 8.3.4 in the
# book does not contain any function named transition, and no
# variable named interval_limits. The function mutate_via_markov_chain
# existing in src/random/mutate.py calls the function draw instead
# of the function transition as done in src/oo/dna_functions.py.

#The following functions are from src/oo/dna_functions.py :

def transition(transition_probabilities):
    interval_limits = []
    current_limit = 0
    for to_base in transition_probabilities:
        current_limit += transition_probabilities[to_base]
        interval_limits.append((current_limit, to_base))
    r = random.random()
    for limit, to_base in interval_limits:
        if r <= limit:
            return to_base

def mutate_via_markov_chain(dna, markov_chain):
    dna_list = list(dna)
    mutation_site = random.randint(0, len(dna_list) - 1)
    from_base = dna[mutation_site]
    to_base = transition(markov_chain[from_base])
    dna_list[mutation_site] = to_base
    return ''.join(dna_list)

# I interpret that the task of the exercise is to re-write the
# function mutate_via_markov_chain above, by merging it with
# the function transition and adding a loop over N mutations.
    
# (The original function mutate_via_markov_chain from file
# src/random/mutate.py is note used here.)

def mutate_via_markov_chain2(dna, markov_chain, N):
    dna_list = list(dna)
    interval_limits = {}
    for from_base in 'ATGC':
        interval_limits[from_base] = []
        limit = 0
        for to_base in markov_chain[from_base]:
            limit += markov_chain[from_base][to_base]
            interval_limits[from_base].append((limit, to_base))
    for n in range(N):
        mutation_site = random.randint(0, len(dna_list) - 1)
        from_base = dna_list[mutation_site]
        r = random.random()
        for limit, to_base in interval_limits[from_base]:
            if r <= limit:
                break
        dna_list[mutation_site] = to_base
    return ''.join(dna_list)

# =============================================================================
# Functions and code taken from src/random/mutate.py:
# =============================================================================

import random

def get_base_frequencies_v2(dna):
        return {base: dna.count(base)/float(len(dna))
                for base in 'ATGC'}

def format_frequencies(frequencies):
    return ', '.join(['%s: %.2f' % (base, frequencies[base])
                      for base in frequencies])

def generate_string_v1(N, alphabet='ACGT'):
    return ''.join([random.choice(alphabet) for i in xrange(N)])

def create_markov_chain():
    markov_chain = {}
    for from_base in 'ATGC':
        # Generate random transition probabilities by dividing
        # [0,1] into four intervals of random length
       slice_points = sorted(
           [0] + [random.random()for i in range(3)] + [1])
       transition_probabilities = \
           [slice_points[i+1] - slice_points[i] for i in range(4)]
       markov_chain[from_base] = {base: p for base, p
                         in zip('ATGC', transition_probabilities)}
    return markov_chain


# Test mutate_via_markov_chain vs. mutate_via_markov_chain2
    
import time
N = 10000
nmutations = 100000
random.seed(10)
mc = create_markov_chain()

random.seed(10)
dna = generate_string_v1(N)
print 'DNA string:', dna[:10], '...', dna[-10:]
print format_frequencies(get_base_frequencies_v2(dna))
t0 = time.clock()
for i in range(nmutations):
    dna = mutate_via_markov_chain(dna, mc)
t1 = time.clock()
print 'DNA string after mutation:', dna[:10], '...', dna[-10:]
print 'Cpu time for mutate_via_markov_chain: %g'%(t1-t0)

print

random.seed(10)
dna = generate_string_v1(N)
print 'DNA string:', dna[:10], '...', dna[-10:]
print format_frequencies(get_base_frequencies_v2(dna))
t0 = time.clock()
dna = mutate_via_markov_chain2(dna, mc, nmutations)
t1 = time.clock()
print 'DNA string after mutation:', dna[:10], '...', dna[-10:]
print 'Cpu time for mutate_via_markov_chain2: %g'%(t1-t0)

