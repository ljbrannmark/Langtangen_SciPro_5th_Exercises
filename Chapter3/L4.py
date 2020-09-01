# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 20:45:55 2019

@author: larsjohan
"""

def L4(x, n=None, epsilon=None, return_n=False):
    #Handle incompatible input arguments:
    if not ( (n is None) ^ (epsilon is None) ):
        print "Error in function L4: Exactly one of the input arguments n and epsilon must be given!"
        if return_n:
            return None, None
        else:
            return None

    x = float(x)
    #If n is specified but not epsilon:
    if (n is not None) and (epsilon is None):
        s = 0
        for i in range(1, n+1):
            s += (1.0/i)*(x/(1+x))**i
        n_terms = n #Set n_terms to be the number of terms   
        
    #If epsilon is specified but not n:
    if (n is None) and (epsilon is not None):
        i = 1
        term = (1.0/i)*(x/(1+x))**i
        s = term
        while abs(term) > epsilon:
            i += 1
            term = (1.0/i)*(x/(1+x))**i
            s += term
        n_terms = i #Set n_terms to be the number of terms
        
    if return_n:
        return s, n_terms
    else:
        return s
