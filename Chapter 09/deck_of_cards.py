# deck_of_cards.py
# Class to create a deck of cards for use in card games.

import random

class deck_of_cards:

    def __init__(self):
        self.cards = [
                      '1S', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', '11S', '12S', '13S',
                      '1C', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', '11C', '12C', '13C',
                      '1H', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', '11H', '12H', '13H',
                      '1D', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', '11D', '12D', '13D'
                     ]
    
    def shuffle(self):
        random.shuffle(self.cards)

    def deal_one(self):
        return self.cards.pop()

    def draw_one(self):
        return self.cards.pop()

    def discard_one(self):
        self.cards.pop()

    def draw_random(self):
        return self.cards.pop([random.randrange(len(self.cards))])

    def return_card(self, card):
        self.cards.insert(random.randrange(len(self.cards)), card)        

    def list_cards(self):
        return self.cards
