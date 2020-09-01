# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:58:33 2019

@author: larsjohan
"""


print '------------------'     # table heading
F = 0                          # start value for F
dF = 10                        # increment of F in loop
while F <= 100:                # loop heading with condition
    C = (F - 32) / (9.0/5)     
    C_hat = (F - 30.0)/2
    print '%.3f %.3f %.3f' % (F, C , C_hat)                
    F = F + dF                 
print '------------------'     # end of table line (after loop)
