# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 23:03:37 2020

@author: lars-johan.brannmark
"""

import random
import sys

class Dice(object):
    def __init__(self, n=1):
        self.n = n   # no of dice

    def throw(self):
        return [random.randint(1,6) \
                for i in range(self.n)]

class Player(object):
    def __init__(self, name, capital, guess_function, ndice):
        self.name = name
        self.capital = capital
        self.guess_function = guess_function
        self.dice = Dice(ndice)


    def play_one_round(self):
        self.guess = self.guess_function(self.dice.n)
        self.throw = sum(self.dice.throw())
        if self.guess == self.throw:
            self.capital += self.guess
        else:
            self.capital -= 1
        self.message()
        self.broke()

    def message(self):
        print '%s guessed %d, got %d' % \
              (self.name, self.guess, self.throw)

    def broke(self):
        if self.capital == 0:
            print '%s lost!' % self.name

# Guessing strategies
def computer_guess(ndice):
    # Any of the outcomes (sum) is equally likely
    return random.randint(ndice, 6*ndice)

def player_guess(ndice):
    if ndice == 1:
        #If there is only one die, all outcomes are equally likely, so choose
        # the outcome that gives the highest reward:
        guess = 6
    else:
        #Otherwise, choose the most likely outcome:
        guess = int(ndice*3.5)
    return guess
        

def play(nrounds, ndice=2):
    player = Player('YOU', nrounds, player_guess, ndice)
    computer = Player('Computer', nrounds, computer_guess, ndice)

    for i in range(nrounds):
        player.play_one_round()
        computer.play_one_round()
        print 'Status: user has %d euro, machine has %d euro\n' % \
              (player.capital, computer.capital)
        if player.capital == 0 or computer.capital == 0:
            break  # terminate game

    if computer.capital > player.capital:
        winner = 'Machine'
    else:
        winner = 'You'
    print winner, 'won!'
    
    return winner

if __name__ == '__main__':
    #Simulate N games and record the number of wins for You and for Machine:
    N = 1000
    you_wins = 0
    machine_wins = 0
    for i in range(N):
        winner = play(nrounds=10, ndice=2)
        if winner == 'You':
            you_wins += 1
        else:
            machine_wins += 1
    print '\np(You win) = ', you_wins/float(N)
    print 'p(Machine wins) = ', machine_wins/float(N)