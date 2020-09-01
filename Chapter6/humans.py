# -*- coding: utf-8 -*-
"""
Created on Sun May  3 00:14:39 2020

@author: lars-johan.brannmark
"""

with open('human_evolution.txt', 'r') as infile:
    lines = infile.readlines()[3:10]
    humans = {line[0:21].strip():
        {'when': line[21:37].strip(), 
         'height': line[37:50].strip(),
         'mass': line[50:62].strip(),
         'brain volume': line[62:].strip()} for line in lines}


print '%-20s %-15s %-12s %-11s %-25s'%('Species','Lived when','Adult','Adult','Brain volume')
print '%-20s %-15s %-12s %-11s %-25s'%('','(mill. yrs)','height (m)','mass (kg)','(cm**3)')
print '-'*80
for key in humans:
    print '%-20s %-15s %-12s %-11s %-25s' %(key, humans[key]['when'], humans[key]['height'], humans[key]['mass'], humans[key]['brain volume'])
print '-'*80