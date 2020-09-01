# -*- coding: utf-8 -*-
"""
Created on Sat May  9 22:25:53 2020

@author: lars-johan.brannmark
"""

p_list = [-0.5] + [0.0]*99 + [2.0]
p_dict = {0: -0.5, 100: 2.0}

print 'List representation:', p_list
print 'Dictionary representation:', p_dict

def eval_poly_list(poly, x):
    return sum([poly[power]*x**power for power in range(len(poly))])

def eval_poly_dict(poly, x):
    return sum([poly[power]*x**power for power in poly])


print 'Evaluation of list polynomial:', eval_poly_list(p_list, 1.05)
print 'Evaluation of dictionary polynomial:', eval_poly_dict(p_dict, 1.05)