# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:57:01 2019

@author: lars-johan.brannmark
"""

F=[]
C=[]

infile = open('Fdeg.dat','r')
lines = infile.readlines()

for line in lines[3:]:
    words = line.split()
    Fval=float(words[2])
    F.append(Fval)
    C.append( (Fval-32)*5/9.0 )
infile.close()

outfile = open('CFtable.dat','w')

for C,F in zip(C,F):
    outfile.write('%6.2f   %6.2f \n' %(C,F))
    
outfile.close()