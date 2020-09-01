# -*- coding: utf-8 -*-
"""
Created on Fri Mar 15 12:16:40 2019

@author: larsjohan
"""

F=range(0,100+1,10)
C=[(f - 32) / (9.0/5) for f in F]
C_hat=[(f - 30.0)/2 for f in F]

conversion = [ [ F[i],C[i],C_hat[i] ] for i in range(len(F)) ]
 
print '------------------'     # table heading
for i in range(len(conversion)):
    for j in range(len(conversion[i])):              
        print '%.3f' % conversion[i][j],
    print
print '------------------'     # end of table line (after loop)