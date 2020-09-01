# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 22:28:40 2020

@author: lars-johan.brannmark
"""

class Hello(object):
        
    def __call__(self, x):
        return 'Hello, %s!' %x

    def __str__(self):
        return 'Hello, World!'