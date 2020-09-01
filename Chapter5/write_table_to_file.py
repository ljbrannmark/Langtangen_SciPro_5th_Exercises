# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 21:05:27 2020

@author: lars-johan.brannmark
"""
import numpy as np

#------------------------------------------------------------------------------

def write_table_to_file(f, xmin, xmax, nx, ymin, ymax, ny, 
                        width=10, decimals=None, 
                        filename='table.dat'):
    # Create array of increasing x values
    x = np.linspace(xmin, xmax, nx+1)
    # Create array of decreasing y values
    y = np.linspace(ymax, ymin, ny+1)
    
    #Define print format pf, based on arguments width and decimals:
    if decimals == None:
        pf = '%' + str(width) + 'g'
    else:
        pf = '%' + str(width) + '.' + str(decimals) + 'g'

    outfile = open(filename, 'w')        
    for i in range(len(y)):
        outfile.write(pf%y[i])
        for j in range(len(x)):
            outfile.write(pf%f(x[j],y[i]))
        outfile.write('\n')        
    outfile.write('\n')
    outfile.write(' '*width)    
    for j in range(len(x)):
        outfile.write(pf%x[j])
    outfile.close()    

#------------------------------------------------------------------------------

def test_write_table_to_file():
    filename = 'tmp.dat'
    write_table_to_file(f=lambda x, y: x + 2*y,
                        xmin=0, xmax=2, nx=4,
                        ymin=-1, ymax=2, ny=3,
                        width=5, decimals=None,
                        filename=filename)
    # Load text in file and compare with expected results
    with open(filename,'r') as infile:
        computed = infile.read()
    expected = """\
    2    4  4.5    5  5.5    6
    1    2  2.5    3  3.5    4
    0    0  0.5    1  1.5    2
   -1   -2 -1.5   -1 -0.5    0

         0  0.5    1  1.5    2"""
    assert computed == expected

#------------------------------------------------------------------------------
    
test_write_table_to_file()