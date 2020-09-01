# -*- coding: utf-8 -*-
"""
Created on Fri Aug 14 21:13:06 2020

@author: lars-johan.brannmark
"""

#Exercise 8.25: Simulate a (simplified) poker game

import random
#random.seed(10)

#We use the Card, Hand and Deck definitions from Deck2.py, with
# additions and modifications:

class Card(object):
    """Representation of a card as a string (suit+rank)."""
    def __init__(self, suit, rank):
        self.card = suit + str(rank)

    def __str__(self):   return self.card
    def __repr__(self):  return str(self)
    
    def get_suit(self):
        #Get suit as a string: 'C', 'D', 'H', or 'S'
        return self.card[0]
    
    def get_rank(self):
        #Get rank as a string: '2', ..., '10', 'J', 'Q', 'K', 'A'
        return self.card[1:]
    
    def get_numrank(self):
        #Get rank as an integer value between 2 and 14 (Ace
        # is given rank 14 here)
        if self.card[1:].isdigit():
            return int(self.card[1:])
        else:
            return 11+['J', 'Q', 'K', 'A'].index(self.card[1:])

class Hand(object):
    """Representation of a hand as a list of Card objects."""
    def __init__(self, list_of_cards):
        self.hand = list_of_cards

    def __str__(self):   return str(self.hand)
    def __repr__(self):  return str(self)

    def rank(self):
        """Compute and return the rank of a hand, from 9
        (Straight flush) to 1 (High card). Applies only to 
        hands containing five cards (poker hands)"""
        if self.check_straight_flush():
            rank = 9
        elif self.check_n_of_a_kind(4):
            rank = 8
        elif self.check_full_house():
            rank = 7
        elif self.check_flush():
            rank = 6
        elif self.check_straight():
            rank = 5
        elif self.check_n_of_a_kind(3):
            rank = 4
        elif self.check_n_of_a_kind(2) == 2:
            rank = 3
        elif self.check_n_of_a_kind(2) == 1:
            rank = 2
        else:
            rank = 1
        return rank
        
    def check_straight_flush(self):
        #Returns True if straight flush
        return self.check_straight() and self.check_flush()
    
    def check_flush(self):
        #Returns True if flush
        suits = [card.get_suit() for card in self.hand]
        return suits.count(suits[0]) == len(suits)
        
    def check_straight(self):
        # Returns True if the ranks of the cards in the hand are
        # in ascending order.
        values1 = [card.get_numrank() for card in self.hand]
        values1.sort()
        straight_1 = values1 == range(min(values1), max(values1)+1)
        #Extra check for the possibility of A being counted as
        #1 instead of 14:
        values2 = [(v-1)%13 + 1 for v in values1]
        values2.sort()
        straight_2 = values2 == range(min(values2), max(values2)+1)
        return straight_1 or straight_2
        
    def check_n_of_a_kind(self, n_of_a_kind):
        """
        Given a hand of cards, return the number of
        n_of_a_kind combinations of ranks.
        For example, with n_of_a_kind=2, the function
        returns the number of pairs in the hand.
        """
        ranks = [card.get_rank() for card in self.hand]
        counter = 0
        already_counted = []
        for rank in ranks:
            if rank not in already_counted and \
                   ranks.count(rank) == n_of_a_kind:
                counter += 1
                already_counted.append(rank)
        return counter
        
    def check_full_house(self):
        #Returns True if full house
        return self.check_n_of_a_kind(3) and self.check_n_of_a_kind(2)
        
    def get_numranks(self, ace_value=14):
        #Get the ranks of the cards in the hand, as a list of
        #integers between 2 and 14 (default), or between 1 and 
        #13 (if ace_value=1)
        ranks = [card.get_numrank() for card in self.hand]
        if ace_value != 14:
            ranks = [(r-1)%13 + 1 for r in ranks]
        return ranks
    
    def get_suits(self):
        #Get the suits of the cards in the hand
        suits = [c.card[0] for c in self.hand]
        return suits
            
    def compare(self, other):
        #Compare with other hand, to be used in sort function
        if self.rank() != other.rank(): #If not a tie:
            c = self.rank() - other.rank()
        #If hand ranks are the same, we need a tie break:
        elif self.rank() == 9:
            #Compare two different straight flush hands:
            max_self = max(self.get_numranks())
            max_other = max(other.get_numranks())
            min_self = min(self.get_numranks())
            min_other = min(other.get_numranks())
            if max_self == 14 and min_self == 2:
                max_self, min_self = 5, 1
            if max_other == 14 and min_other ==2:
                max_other, min_other = 5, 1
            c = max_self - max_other
        elif self.rank() == 8:
            #Compare two different four-of-a-kind hands:
            self_ranks = self.get_numranks()
            other_ranks = other.get_numranks()
            self_set = list(set(self_ranks))
            other_set = list(set(other_ranks))
            self_count = [(self_ranks.count(self_set[i]), self_set[i]) \
                          for i in range(len(self_set))]
            other_count = [(other_ranks.count(other_set[i]), other_set[i]) \
                           for i in range(len(other_set))]
            self_4_val = [self_count[i][1] for i in range(2) if self_count[i][0] == 4][0]
            other_4_val = [other_count[i][1] for i in range(2) if other_count[i][0] == 4][0]
            c = self_4_val - other_4_val
        elif self.rank() == 7:
            #Compare two different full house hands:
            self_ranks = self.get_numranks()
            other_ranks = other.get_numranks()
            self_set = list(set(self_ranks))
            other_set = list(set(other_ranks))
            self_count = [(self_ranks.count(self_set[i]), self_set[i]) \
                          for i in range(len(self_set))]
            other_count = [(other_ranks.count(other_set[i]), other_set[i]) \
                           for i in range(len(other_set))]
            self_3_val = [self_count[i][1] for i in range(2) if self_count[i][0] == 3][0]
            other_3_val = [other_count[i][1] for i in range(2) if other_count[i][0] == 3][0]
            c = self_3_val - other_3_val
        elif self.rank() == 6:
            #Compare two different flush hands (similar to high card):
            self_ranks = sorted(self.get_numranks(), reverse=True)
            other_ranks = sorted(other.get_numranks(), reverse=True)
            ranks_diff = [self_ranks[i] - other_ranks[i] for i in range(len(self_ranks))]
            c = next((v for v in ranks_diff if v != 0))
        elif self.rank() == 5:
            #Compare two different straight hands:
            self_ranks = self.get_numranks()
            other_ranks = other.get_numranks()
            c = max(self_ranks) - max(other_ranks)
        elif self.rank() == 4:
            #Compare two different three-of-a-kind hands:
            self_ranks = self.get_numranks()
            other_ranks = other.get_numranks()
            self_set = list(set(self_ranks))
            other_set = list(set(other_ranks))
            self_count = [(self_ranks.count(self_set[i]), self_set[i]) \
                          for i in range(len(self_set))]
            other_count = [(other_ranks.count(other_set[i]), other_set[i]) \
                           for i in range(len(other_set))]
            self_3_val = [self_count[i][1] for i in range(3) if self_count[i][0] == 3][0]
            other_3_val = [other_count[i][1] for i in range(3) if other_count[i][0] == 3][0]
            c = self_3_val - other_3_val
        elif self.rank() == 3:
            #Compare two different two-pairs hands:
            self_ranks = sorted(self.get_numranks(), reverse=True)
            other_ranks = sorted(other.get_numranks(), reverse=True)
            self_set = list(set(self_ranks))
            other_set = list(set(other_ranks))
            self_count = [(self_ranks.count(self_set[i]), self_set[i]) \
                          for i in range(len(self_set))]
            other_count = [(other_ranks.count(other_set[i]), other_set[i]) \
                           for i in range(len(other_set))]
            self_2_val = [self_count[i][1] for i in range(3) if self_count[i][0] == 2]
            other_2_val = [other_count[i][1] for i in range(3) if other_count[i][0] == 2]
            #Compare the pairs of highest rank:
            c = max(self_2_val) - max(other_2_val)
            if c == 0:
                #If both hands have the same highest-rank pair,
                #then compare the lowest-rank pairs:
                c = min(self_2_val) - min(other_2_val)
            if c == 0:
                #If also the lowest rank pairs have same rank, then
                #compare the remaining card:
                self_1_val = [self_count[i][1] for i in range(3) if self_count[i][0] == 1][0]
                other_1_val = [other_count[i][1] for i in range(3) if other_count[i][0] == 1][0]
                c = self_1_val - other_1_val
            
        elif self.rank() == 2:
            #Compare two different pair hands:
            self_ranks = sorted(self.get_numranks(), reverse=True)
            other_ranks = sorted(other.get_numranks(), reverse=True)
            self_set = list(set(self_ranks))
            other_set = list(set(other_ranks))
            self_count = [(self_ranks.count(self_set[i]), self_set[i]) \
                          for i in range(len(self_set))]
            other_count = [(other_ranks.count(other_set[i]), other_set[i]) \
                           for i in range(len(other_set))]
            self_2_val = [self_count[i][1] for i in range(4) if self_count[i][0] == 2][0]
            other_2_val = [other_count[i][1] for i in range(4) if other_count[i][0] == 2][0]
            c = self_2_val - other_2_val
            #If both hands have pair of same rank, then look at the remaining cards:
            if c == 0:
                self_ranks.remove(self_2_val)    
                self_ranks.remove(self_2_val)  
                other_ranks.remove(other_2_val)    
                other_ranks.remove(other_2_val)
                self_ranks.sort(reverse=True)
                other_ranks.sort(reverse=True)
                ranks_diff = [self_ranks[i] - other_ranks[i] \
                              for i in range(len(self_ranks))]
                c = next((v for v in ranks_diff if v != 0))
        elif self.rank() == 1:
            #Compare two different high-card hands:
            self_ranks = sorted(self.get_numranks(), reverse=True)
            other_ranks = sorted(other.get_numranks(), reverse=True)
            ranks_diff = [self_ranks[i] - other_ranks[i] \
                          for i in range(len(self_ranks))]
            c = next((v for v in ranks_diff if v != 0))
        else:
            c = 0
        return c
    
    def discard(self):
        #Discard cards from a hand, according to a 
        #very simple poker strategy.
        hand_rank = self.rank()
        card_ranks = self.get_numranks()
        card_suits = self.get_suits()
        discard_list = []
        #
        if hand_rank == 1:
        #If high card, discard all cards of rank less than 10.
        #(Disregard the chance of getting flush, straight etc.)
            discard_list = [self.hand[i] for i in range(len(card_ranks)) \
                           if card_ranks[i] < 10]
            for i in range(len(discard_list)):
                self.hand.remove(discard_list[i])
        #
        if hand_rank == 2:
            #If pair, discard the three cards not in the pair
            #
            #Find the list indices to the cards not in the pair
            discard_ind = [i for i in range(len(card_ranks)) \
                           if card_ranks.count(card_ranks[i])!=2]
            card1 = self.hand[discard_ind[0]]
            card2 = self.hand[discard_ind[1]]
            card3 = self.hand[discard_ind[2]]
            self.hand.remove(card1)
            self.hand.remove(card2)
            self.hand.remove(card3)
            discard_list = [card1, card2, card3]
        if hand_rank == 3:
            #If 2 pairs, discard the card not in the pairs
            #
            #Find the list index to the card not in the pair
            discard_ind = [i for i in range(len(card_ranks)) \
                           if card_ranks.count(card_ranks[i])!=2]
            card1 = self.hand[discard_ind[0]]
            self.hand.remove(card1)
            discard_list = [card1]
        if hand_rank == 4:
            #If three-of-a-kind, discard the other two cards
            #
            #Find the list indices to the other cards
            discard_ind = [i for i in range(len(card_ranks)) \
                           if card_ranks.count(card_ranks[i])!=3]
            card1 = self.hand[discard_ind[0]]
            card2 = self.hand[discard_ind[1]]
            self.hand.remove(card1)
            self.hand.remove(card2)
            discard_list = [card1, card2]
        return discard_list
            

class Deck(object):
    """Representation of a deck as a list of Card objects."""

    def __init__(self):
        ranks = ['A', '2', '3', '4', '5', '6', '7',
                 '8', '9', '10', 'J', 'Q', 'K']
        suits = ['C', 'D', 'H', 'S']
        self.deck = [Card(s,r) for s in suits for r in ranks]
        random.shuffle(self.deck)

    def hand(self, n=1):
        """Deal n cards. Return hand as a Hand object."""
        hand = Hand([self.deck[i] for i in range(n)])
        del self.deck[:n]         # remove cards
        return hand

    def deal(self, cards_per_hand, no_of_players):
        """Deal no_of_players hands. Return list of Hand obj."""
        return [self.hand(cards_per_hand) \
                for i in range(no_of_players)]

    def putback(self, card):
        """Put back a card under the rest."""
        self.deck.append(card)
        
    def shuffle(self):
        random.shuffle(self.deck)

    def __str__(self):
        return str(self.deck)

    def __repr__(self):
        return str(self)

    def __len__(self):
        return len(self.deck)
    
    

# =============================================================================
#     Set up a poker game (five card draw, without betting):
# =============================================================================


#Decide number of players
N_players = 5

deck = Deck()      #Initialize deck of cards
discard_heap = []  #Initialize empty heap for discarded cards

#Deal five cards to player 0, 1, ..., N_players-1
players = deck.deal(5, N_players)

for player in players:
    #Eeach player inspects his hand and discards the
    #unwanted cards according to the simple strategy in
    #function Hand.discard:
    discard_cards = player.discard()
    
    #Throw the discarded cards on the heap
    discard_heap += discard_cards
    
    #Deal new cards to player from the deck
    try:
        new_cards = deck.deal(len(discard_cards),1)[0]
    except:
        #If deck runs out of cards, put back heap
        # of discarded cards, and shuffle:
        for c in discard_heap:
            deck.putback(c)
        discard_heap = []
        deck.shuffle()
        new_cards = deck.deal(len(discard_cards),1)[0]
    player.hand.extend(new_cards.hand)

#Put back all discarded cards in the deck and shuffle the deck:
for c in discard_heap:
    deck.putback(c)
discard_heap = []
deck.shuffle()

#Game is over: compare hands to find winner:
players_enum = [p for p in enumerate(players)]
players_enum.sort(cmp=lambda x, y: Hand.compare(x[1],y[1]), reverse=True)
ranks = [p[1].rank() for p in players_enum]

rankstr=['', 'High card', 'Pair', 'Two pairs', 'Three of a kind',\
         'Straight', 'Flush', 'Full House', 'Four of a kind', 'Straight flush']

print "Winner is player %d with hand %s (%s): "\
%(players_enum[0][0], players_enum[0][1], rankstr[Hand.rank(players_enum[0][1])])
print "Second best is player %d with hand %s (%s): "\
%(players_enum[1][0], players_enum[1][1], rankstr[Hand.rank(players_enum[1][1])])

print
print "Hands of all players (in order of the ranks of the hands):"
for i in range(len(players)):
    print 'Player %d: %s (%s)'%(players_enum[i][0], players_enum[i][1],rankstr[Hand.rank(players_enum[i][1])])


