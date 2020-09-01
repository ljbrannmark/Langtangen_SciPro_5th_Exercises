# -*- coding: utf-8 -*-
"""
Created on Fri Mar 01 13:07:43 2019

@author: larsjohan
"""

#Some physical constants:
m_e=9.1094e-31
e=1.6022e-19
eps_0=8.8542e-12
h=6.6261e-34

E=[]
deltaE=[]

for i in range(0,20):
    n=i+1
    E.append(-(m_e * e**4)/(8 * eps_0**2 * h**2)*1.0/n**2)
    print 'n=%g , E_n=%.4g' %(n,E[i])

print

for f in range(0,5):                         #Loop over rows f=0,1,...,4
    tmpList=[E[i]-E[f] for i in range(0,5)]  #Use list comprehension to generate columns 0,1,...,4 for row f
    deltaE.append(tmpList)                   


for f in range(len(deltaE)):
    for i in range(len(deltaE[f])):
        print '%12.4g' %(deltaE[f][i]),
        
    print

    
    
    
    

         
