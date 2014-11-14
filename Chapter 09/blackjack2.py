# blackjack.py

import random

class Deck:

    def __init__(self, highest):
        self.highest = highest
        self.value = 1

    def dealOne(self):
        self.value = random.randrange(2,self.highest+1)
        return self.value

def main():
    printIntro()
    n, start = getInputs()
    busts = simNGames(n, start)
    printSummary(busts, n)

def printIntro():
    print("This program will simulate a game of blackjack")
    print("from the dealer's perspective. It will determine")
    print("the likelyhood of the dealer busting.\n")

def getInputs():
    n = int(input("How many games to simulate? "))
    start = int(input("What card number should the dealer start with (2-11)? "))
    return n, start

def simNGames(n, start):
    busts = 0
    for i in range(n):
        busts += simOneGame(start)
    return busts

def simOneGame(start):
    bust = 0
    deck = Deck(11)
    hand = start
    card = 0
    Aces = 0
    while hand not in range(17,22):
        card = (deck.dealOne())
        if card == 11:
            Aces += 1
        hand += card
        if hand > 21 and Aces > 0:
            hand -= 10
            Aces -= 1
        if hand > 21:
            break
    if hand > 21:
        bust = 1
    return bust               

def printSummary(busts, n):
    print("Number of games simulate: {}".format(n))
    print("Dealer busts: {0} {1:0.2%}".format(busts, busts/n))

if __name__ == "__main__": main()
