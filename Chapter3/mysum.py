# -*- coding: utf-8 -*-
"""
Created on Sun Jun 23 23:00:15 2019

@author: larsjohan
"""

def mysum(L):
    s=type(L[0])()   #Ensure the empty accumulator variable s 
                     #is of the same type as the first 
                     #element in list L
    for i in range(len(L)):
        s += L[i]
    return s

L0=[1,3,5,-5]
S0=mysum(L0)

L1=[[1, 2], [3, 4], [5, 6]]
S1=mysum(L1)

L2=['Hello, ','World!']
S2=mysum(L2)
