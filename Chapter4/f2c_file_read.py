# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 23:24:15 2019

@author: lars-johan.brannmark
"""

infile = open("temp_data.txt",'r')
lines = infile.readlines()
infile.close()
line = lines[3]
words = line.split()
F = float(words[2])
C = (F-32)*5/9.0
print C