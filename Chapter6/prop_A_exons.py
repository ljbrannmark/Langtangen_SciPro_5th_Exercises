# -*- coding: utf-8 -*-
"""
Created on Wed May 20 23:16:57 2020

@author: lars-johan.brannmark
"""

def get_exons(gene, exon_regions):
    return ''.join(
            [gene[start:end] for start, end in 
             [exon_regions[i] for i in range(len(exon_regions))]]
            )

def get_introns(gene, exon_regions):
    return gene[0:exon_regions[0][0]] + \
    ''.join(
            [gene[start:end] for start, end in 
             [(exon_regions[i][1], exon_regions[i+1][0]) 
             for i in range(len(exon_regions)-1)]] 
            ) + \
            gene[exon_regions[-1][1]:]

def get_base_frequencies(dna):
    return {base: dna.count(base)/float(len(dna)) for base in dna}

def read_dnafile(filename):
    return ''.join([line.strip() for line in open(filename, 'r').readlines()])

def read_exon_regions(filename):
    return [tuple(int(x) for x in line.split())
            for line in open(filename, 'r')]
    
lactase_gene = read_dnafile('lactase_gene.txt')
lactase_exon_regions = read_exon_regions('lactase_exon.tsv')

exon_dna = get_exons(lactase_gene, lactase_exon_regions)
intron_dna = get_introns(lactase_gene, lactase_exon_regions)

print 'Frequency of base A in lactase gene exons: %.18f' %get_base_frequencies(exon_dna)['A']
print 'Frequency of base A in lactase gene introns: %.18f' %get_base_frequencies(intron_dna)['A']
