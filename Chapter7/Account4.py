# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:29:05 2020

@author: lars-johan.brannmark
"""

class Account(object):
    def __init__(self, name, account_number, initial_amount):
        self.name = name
        self.no = account_number
        self.balance = initial_amount
        
    def __iadd__(self, amount):
        self.balance += amount
        return self
    
    def __isub__(self, amount):
        self.balance -= amount
        return self
    
    def __str__(self):
        s = '%s, %s, balance: %d' % \
            (self.name, self.no, self.balance)
        return s
    
    def __repr__(self):
        return "Account('%s', '%s', %d)" %(self.name, self.no, self.balance)

    def deposit(self, amount):
        self += amount

    def withdraw(self, amount):
        self -= amount

    def dump(self):
        s = '%s, %s, balance: %d' % \
            (self.name, self.no, self.balance)
        print s
        
def test_Account():
    a1 = Account('John Olsson', '19371554951', 10000)
    a2 = eval(repr(a1))
    for i in range(100):
        a1 += 100
        a1 -= 50
        a2.deposit(100)
        a2.withdraw(50)
    print a1
    print a2
    a1.dump()
    a2.dump()
    msg = 'Error in class Account!'
    success = str(a1) == str(a2)
    assert success, msg
    
test_Account()