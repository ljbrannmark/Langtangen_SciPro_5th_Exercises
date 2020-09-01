# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:39:57 2020

@author: lars-johan.brannmark
"""

import time

class AccountP(object):
    def __init__(self, name, account_number, initial_amount=0):
        self._name = name
        self._no = account_number
        self._transactions = [{time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()): 
            initial_amount}]

    def deposit(self, amount):
        self._transactions.append({time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()): 
            amount})

    def withdraw(self, amount):
        self._transactions.append({time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime()): 
            -amount})

    def get_balance(self):
        return sum([self._transactions[i].values()[0] for 
                    i in range(len(self._transactions))])
    
    def print_transactions(self):
        for transaction in self._transactions:
            print '%s : %s'%(transaction.keys()[0], transaction.values()[0])

    def dump(self):
        s = '%s, %s, balance: %s' % \
            (self._name, self._no, self.get_balance())
        print s
        

    
