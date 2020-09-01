# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 15:58:33 2019

@author: larsjohan
"""

print '------------------'     # table heading
F = 0                          # start value for F
dF = 10                        # increment of F in loop
while F <= 100:                # loop heading with condition
    C = (F - 32) / (9.0/5)     # 1st statement inside loop
    print F, C                 # 2nd statement inside loop
    F = F + dF                 # 3rd statement inside loop
print '------------------'     # end of table line (after loop)