# -*- coding: utf-8 -*-
"""
Created on Tue Dec 10 22:32:57 2019

@author: lars-johan.brannmark
"""

def power3_identity(A=-100, B=100, n=1000):
    import random
    failures = 0
    for i in range(n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        failures += int( (a*b)**3 != a**3 * b**3 )
    return failures/float(n)

def equal(expr1, expr2, A=-100, B=100, n=500):
    import random, sys
    failures = 0
    for i in range(n):
        a = random.uniform(A, B)
        b = random.uniform(A, B)
        try:
            failures += int ( eval(expr1) != eval(expr2) )
        except ValueError:
            print "Error in function equal(): Value of a and/or b is out of",
            print "range for the computation of %s == %s."%(expr1,expr2),
            print "Consider using other parameters A and B in call to function",
            print "equal('%s','%s',A,B,n)\n" %(expr1,expr2)
            sys.exit(1)
    return failures/float(n)

from math import exp, log, sin, cos, sinh, tan
print "4.23 a) ---------------------------------------------------\n"
print "Function power3_identity: Fraction of failures for \
(a*b)**3 == a**3 * b**3: %.3g\n" %power3_identity()

print "4.23 b)---------------------------------------------------\n"
print "Function equal: Fraction of failures for \
(a*b)**3 == a**3 * b**3: %.3g\n" %equal('(a*b)**3', 'a**3*b**3')

print "Function equal: Fraction of failures for \
exp(a+b) == exp(a)*exp(b): %.3g\n" %equal('exp(a+b)', 'exp(a)*exp(b)')

print "Function equal: Fraction of failures for \
log(a**b) == b*log(a): %.3g\n" %equal('log(a**b)', 'b*log(a)', A=1, B=100)

expr=[('a-b','-(b-a)'),
      ('a/b','1/(b/a)'),
      ('(a*b)**4','a**4*b**4'),
      ('(a+b)**2','a**2+2*a*b+b**2'),
      ('(a+b)*(a-b)','a**2-b**2'),
      ('exp(a+b)','exp(a)*exp(b)'),
      ('log(a**b)','b*log(a)'),
      ('log(a*b)','log(a)+log(b)'),
      ('a*b','exp(log(a)+log(b))'),
      ('1/(1/a+1/b)','a*b/(a+b)'),
      ('a*(sin(b)**2+cos(b)**2)','a'),
      ('sinh(a+b)','exp(a)*exp(b)-exp(-a)*exp(-b)/2'),
      ('tan(a+b)','sin(a+b)/cos(a+b)'),
      ('sin(a+b)','sin(a)*cos(b)+sin(b)*cos(a)')]

print "4.23 c)---------------------------------------------------\n"
outfile = open('Ex_4_23_MathIdentities.txt','w')
print "%-45s%18s"%('Expressions:','Failure rate:')
outfile.write("%-45s%18s"%('Expressions:','Failure rate:')+'\n')
for e in expr:
     str = "%-45s%18.3g"%(e[0]+', '+e[1],equal(e[0], e[1], A=1, B=2, n=1000))
     print str
     outfile.write(str+'\n')
outfile.close()
