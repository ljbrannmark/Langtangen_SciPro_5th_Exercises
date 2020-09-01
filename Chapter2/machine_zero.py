# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:08:38 2019

@author: larsjohan
"""

eps=1.0
while 1.0 != 1.0 + eps:
    print '............', eps
    eps = eps / 2.0
print 'Final eps:', eps