# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 21:50:17 2020

@author: lars-johan.brannmark
"""

from Deck import *
from cards import same_rank, same_suit
from math import factorial as f

def nCk(n,k):
    return int(f(n) / f(k) / f(n-k))

#Number of experiments
N = 2000000

##############################
##############################
s_2pairs = 0
#Run N experiments
for i in range(N):
    #In each experiment, draw ten random five-card hands and count the
    # hands that contain exactly two pairs
    deck = Deck()
    players = deck.deal(5, 10)
    for hand in players:
        s_2pairs += same_rank(hand, 2) == 2

#Divide by the total number of hands to get the estimated probability:
p_2pairs = s_2pairs/float(N*10)
print 'Probability of 2 pairs among five cards: %g' %p_2pairs
print '(True probability: %g)' %(nCk(13,2)*nCk(4,2)*nCk(4,2)*11*4/float(nCk(52,5)))
##############################
##############################
s_4_5_samesuit = 0
#Run N experiments
for i in range(N):
    #In each experiment, draw ten random five-card hands and count the
    # hands that contain at least four cards of same suit
    deck = Deck()
    players = deck.deal(5, 10)
    for hand in players:
        s_4_5_samesuit += same_suit(hand).values()[0] >= 4

#Divide by the total number of hands to get the estimated probability:
p_4_5_samesuit = s_4_5_samesuit/float(N*10)
print 'Probability of 4 or 5 of same suit among 5 cards: %g' %p_4_5_samesuit
print '(True probability: %g)' %((nCk(13,4)*4*13*3 + nCk(13,5)*4)/float(nCk(52,5)))
##############################
##############################
s_4kind = 0
#Run N experiments
for i in range(N):
    #In each experiment, draw ten random five-card hands and count the
    # hands that contain four-of-a-kind
    deck = Deck()
    players = deck.deal(5, 10)
    for hand in players:
        s_4kind += same_rank(hand, 4)

#Divide by the total number of hands to get the estimated probability:
p_4kind = s_4kind/float(N*10)
print 'Probability of 4-of-a-kind among 5 cards: %g' %p_4kind
print '(True probability: %g)' %(13*12*4/float(nCk(52,5)))