# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 23:38:03 2019

@author: larsjohan
"""

def count_substr(string,substring):
    n=len(substring)
    c=0
    for i in range(len(string)):
        if string[i]==substring[0]:
            if string[i:i+n]==substring:
                c+=1
    return c


### Alternative, more compact version
# 
#def count_substr(string,substring):
#    c=0
#    for i in range(len(string)):
#        if string[i:i+len(substring)]==substring:
#            c+=1
#    return c