# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 09:54:53 2020

@author: lars-johan.brannmark
"""

class Person(object):
    def __init__(self, name='', address='', phone='', birthday='', nationality=''):
        self.name = name
        self.address = address
        self.phone = phone
        self.birthday = birthday
        self.nationality = nationality
        
    def __str__(self):
        s = '\n'.join(['%s: '%v+str(eval('self.'+v)) for v in dir(self) if v[0:2]!='__' and len(eval('self.'+v))!=0])
        return s
    
class Worker(Person):
    def __init__(self, name, company='', company_address='', job_phone='', **kwargs):
        Person.__init__(self, name, **kwargs)
        self.company = company
        self.company_address = company_address
        self.job_phone = job_phone
        
class Scientist(Worker):
    def __init__(self, name, discipline='', science_type=[], **kwargs):
        Worker.__init__(self, name, **kwargs)
        self.discipline = discipline
        self.science_type = science_type
        
class Researcher(Scientist):
    pass

class Postdoc(Scientist):
    pass

class Professor(Scientist):
    pass
        
pe = Person('Helmer Bryd', address='Gimogatan 9')
wo = Worker('Helmer Bryd', address='Gimogatan 9', company='Olofssons Bageri', company_address='St Olofsgatan 4', job_phone='070-5403475')
sc = Scientist('Johan Bååth', address = 'Storgatan 12')
re = Researcher('Peter Faxman', address = 'Dragarbrunnsgatan 8', discipline='Physics', science_type=['Experimental', 'Computational'])
po = Postdoc('Alma Mahler', address = 'Vaksalagatan 11', discipline='Musicology', science_type=['Behavioral'], company='Universität Freiburg')
pr = Professor('Johan Bååth', address = 'Storgatan 12', birthday = '1974-09-20', nationality='Swedish', job_phone='073-6783465', company='KTH')

for person in [pe, wo, sc, re, po, pr]:
    print person
    print '-'*50