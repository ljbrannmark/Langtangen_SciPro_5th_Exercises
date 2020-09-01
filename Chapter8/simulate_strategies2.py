# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 21:44:37 2020

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
    def __init__(self, name, capital, guess_function, ndice, output=True):
        self.name = name
        self.capital = capital
        self.guess_function = guess_function
        self.dice = Dice(ndice)
        self.output = output

    def play_one_round(self):
        self.guess = self.guess_function(self.dice.n)
        self.throw = sum(self.dice.throw())
        if self.guess == self.throw:
            self.capital += self.guess
        else:
            self.capital -= 1
        if self.output:
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
        

def play(nrounds, ndice_player=2, ndice_computer=2, output=True):
    player = Player('YOU', nrounds, player_guess, ndice_player, output)
    computer = Player('Computer', nrounds, computer_guess, ndice_computer, output)

    for i in range(nrounds):
        player.play_one_round()
        computer.play_one_round()
        if output:
            print 'Status: user has %d euro, machine has %d euro\n' % \
                  (player.capital, computer.capital)
        if player.capital == 0 or computer.capital == 0:
            break  # terminate game

    if computer.capital > player.capital:
        winner = 'Machine'
    else:
        winner = 'You'
    if output:
        print winner, 'won!'
        
    return winner

if __name__ == '__main__':
    N = 1000
    #Try out a range of ndice for the player, while the computer always selects
    # a random number of dice between 2 and 20. For each choice of player's 
    #number of dice, record the number of wins for player and machine:
    max_dice = 20
    you_wins = [0]*max_dice
    machine_wins = [0]*max_dice
    #Do for ndice_player = 1, 2, ..., max_dice
    for n in range(0, max_dice):
        #Simulate N games and record the number of wins for player and 
        #for Machine:
        for i in range(N):
            winner = play(nrounds=10, ndice_player=n+1, ndice_computer=random.randint(2, 20), output=False)
            if winner == 'You':
                you_wins[n] += 1
            else:
                machine_wins[n] += 1
    for n in range(0, max_dice):
        print '\np(You win|ndice_player = %d) = '%(n+1), you_wins[n]/float(N)
        print 'p(Machine wins|ndice_player = %d) = '%(n+1), machine_wins[n]/float(N)