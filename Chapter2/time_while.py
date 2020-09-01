# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 22:12:42 2019

@author: larsjohan
"""

import time
t0=time.time()
while time.time() - t0 < 10:
    print '....I like while loops!'
    time.sleep(2)
print 'Oh, no - the loop is over.'