# -*- coding: utf-8 -*-
"""
Created on Sun Dec  1 22:31:15 2019

@author: lars-johan.brannmark
"""

def read_data(fname):
    t=[]
    infile = open(fname)
    lines = infile.readlines()
    infile.close()
    v0 = float(lines[0].split()[1])
    for line in lines[2:]:
        values = line.split()
        for value in values:
            t.append(float(value))
    return v0, t


def test_read_data():
    v0 = 3.00
    t = [[0.1247,    0.4472,    0.5560,    0.3262,    0.6037,    0.1858],
         [0.0754,    0.4263,    0.4108,    0.2119,    0.5167],
         [0.2434,    0.5634,    0.3075],
         [0.0789,    0.5617],
         [0.4708,    0.3544,    0.5413],
         [0.1888,    0.4847,    0.0726,    0.1620,    0.0013,    0.2978,    0.5281],
         [0.4190,    0.4786,    0.2368,    0.6116]]
    
    fname = 'test_ball_data.dat'
    outfile = open(fname,'w')
    outfile.write('v0: %.2f\n' % (v0))
    outfile.write('t:\n')
    for r in t:
        for c in r:
            outfile.write('%-10.4f' % c)
        outfile.write('\n')
    outfile.close()
    
    v0_test, t_test = read_data(fname)
    success = True
    if v0_test != v0:
        success = False
    t_flat = [item for row in t for item in row]
    if t_flat != t_test:
        success = False
    msg = 'Function read_data(fname) failed!'
    assert success, msg
    
    
def y(v0,t):
    g = 9.81
    return v0*t - 0.5*g*t**2
          
  
def write_sorted_data(inFileName,outFileName):
    v0, t = read_data(inFileName)
    t.sort()
    outfile = open(outFileName,'w')
    outfile.write('t:        y:\n')
    for i in range(len(t)):
        outfile.write('%-10.4f%-10.4f\n' %(t[i],y(v0,t[i])))
    outfile.close()
        
    
            
            
    
    