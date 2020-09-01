# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 14:15:36 2019

@author: larsjohan
"""

initial_amount=100
p=5.0 #interest rate
amount=initial_amount
years=0
while amount <= 1.5*initial_amount:
    amount += + p/100*amount
    years+=1
print years