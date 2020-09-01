# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 22:11:36 2020

@author: lars-johan.brannmark
"""
#Exercise 8.26. Re-using code from birth_policy.py

import numpy as np
MALE = 1;  FEMALE = 2

def get_children(n, male_portion, fertility):
    if n == 0: return []
    n = int(fertility*n)  # not all n couples get a child
    r = np.random.random(n)
    children = np.zeros(n, int)
    children[r <  male_portion] = MALE
    children[r >= male_portion] = FEMALE
    return children
    
def advance_generation(parents, policy='one child',
                       male_portion=0.5, fertility=1.0,
                       law_breakers=0, wanted_children=4):
    """
    Given a generation of parents (random integers with
    values MALE or FEMALE), compute the next generation
    of children.
    Return: array of children (MALE and FEMALE values),
    and the maximum number of children found in a family.
    """
    males = len(parents[parents==MALE])
    females = len(parents) - males
    couples = min(males, females)

    if policy == 'one child':
        # Each couple gets one child.
        children = get_children(couples, male_portion, fertility)
        max_children = 1
    elif policy == 'one son':
        # Each couple can continue with a new child until 
        # they get a son.

        # First try.
        children = get_children(couples, male_portion, fertility)
        max_children = 1
        # Continue with getting a new child for each daughter.
        daughters = children[children == FEMALE]
        while len(daughters) > 0:
            new_children = get_children(len(daughters),
                                        male_portion, fertility)
            children = np.concatenate((children, new_children))
            daughters = new_children[new_children == FEMALE]
            max_children += 1
    # A portion law_breakers breaks the law and gets wanted_children.
    illegals = get_children(int(len(children)*law_breakers)*wanted_children,
                            male_portion, fertility=1.0)
    children = np.concatenate((children, illegals))
    return children, max_children

N = 1000000
male_portion = 0.51
fertility = 0.92
law_breakers = 0.06
wanted_children = 6

generations = 10
# Start with a "perfect" generation of parents.
start_parents = get_children(N, male_portion=0.5, fertility=1.0)
parents = start_parents.copy()
pop_size = np.zeros(generations, dtype=int)
print 'one son policy, start: %d' % len(parents)
for i in range(generations):
    parents, mc = advance_generation(parents, 'one son',
                                     male_portion, fertility,
                                     law_breakers, wanted_children)
    pop_size[i] = len(parents)
    print '%3d: %d (max children in a family: %d)' % \
          (i+1, pop_size[i], mc)

r = np.array([pop_size[n]/float(pop_size[n-1])-1.0 for n in range(1, generations)])

print '\nAverage of r = x(n)/x(n-1) - 1 over %d generations: %g'%(generations,r.mean())
print 'Growth factor r is approx. %.3g percent.' %(r.mean()*100)
