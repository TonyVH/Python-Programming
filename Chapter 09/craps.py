# craps.py

import random

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = random.randrange(1, self.sides+1)

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

def main():
    printIntro()
    n = getInput()
    wins = simNGames(n)
    printSummary(wins, n)

def printIntro():
    print("This program will simulate a game of craps.")
    print("It will determine the odds of winning based on")
    print("how many games are won and lost.\n")

def getInput():
    n = int(input("How many games should be simulated? "))
    return n

def simNGames(n):
    wins = 0
    for i in range(n):
        wins += simOneGame()
    return wins

def simOneGame():
    result = 0
    d1 = MSDie(6)
    d2 = MSDie(6)
    d1.roll()
    d2.roll()
    value = d1.getValue() + d2.getValue()
    if value == 7 or value == 11:
        result = 1
    elif value == 2 or value == 3 or value == 12:
        result = 0
    else:
        d1.roll()
        d2.roll()
        if d1.getValue() + d2.getValue() == value:
            result = 1
        else:
            while d1.getValue() + d2.getValue() != value and d1.getValue() + d2.getValue() != 7:
                if d1.getValue() + d2.getValue() == 7:
                    result = 0
                elif d1.getValue() + d2.getValue() == value:
                    result = 1
                else:
                    d1.roll()
                    d2.roll()
    return result

def printSummary(wins, n):
    print("Number of games simulated: {}".format(n))
    print("Wins: {}".format(wins))
    print("Win Percentage: {0:0.2%}".format(wins/n))

if __name__ == "__main__": main()
