# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:55:04 2019

@author: larsjohan
"""

numbers = range(10)
print numbers

for n in numbers:
    i = len(numbers)/2
    del numbers[i]
    print 'n=%d, del %d' % (n,i), numbers

    
    