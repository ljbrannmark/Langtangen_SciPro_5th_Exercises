# -*- coding: utf-8 -*-
"""
Created on Thu Jun 18 23:56:27 2020

@author: lars-johan.brannmark
"""

class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        self.transactions = 0

    def deposit(self, amount):
        self.balance += amount
        self.transactions += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.transactions += 1
        
    def dump(self):
        s = '%s, %s, balance: %s, no. of transactions: %s' % \
            (self.name, self.no, self.balance, self.transactions)
        print s
        
def test_Account():        
    a1 = Account('John Olsson', '19371554951', 10000)
    a2 = Account('Liz Olsson',  '19371564761', 10000)
    for i in range(100):
        a1.deposit(100)
        a1.withdraw(50)
        a2.deposit(100)
        a2.withdraw(50)
    msg = 'Error in class Account!'
    success = a1.balance==15000 and a2.balance==15000 and \
    a1.transactions==200 and a2.transactions==200
    assert success, msg
    
test_Account()