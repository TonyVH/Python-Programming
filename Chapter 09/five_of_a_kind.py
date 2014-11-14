# five_of_a_kind.py

import random

class MSDie:

    def __init__(self, sides):
        self.sides = sides
        self.value = 1

    def roll(self):
        self.value = random.randrange(1, self.sides+1)

    def getValue(self):
        return self.value

def main():
    printIntro()
    n = rollDice()
    printSummary(n)

def printIntro():
    print("This program will determine how many rolls it will take")
    print("to roll five-of-a-kind on a single roll.\n")

def rollDice():
    n = 1
    d1, d2, d3, d4, d5 = MSDie(6), MSDie(6), MSDie(6), MSDie(6), MSDie(6)
    d1.roll()
    d2.roll()
    d3.roll()
    d4.roll()
    d5.roll()
    while not fiveOfAKind(d1.getValue(), d2.getValue(), d3.getValue(), d4.getValue(), d5.getValue()):
        d1.roll()
        d2.roll()
        d3.roll()
        d4.roll()
        d5.roll()
        n += 1
    return n

def fiveOfAKind(d1, d2, d3, d4, d5):
    if d1 == d2 and d2 == d3 and d3 == d4 and d4 == d5:
        return True
    else:
        return False

def printSummary(n):
    print("It took {} rolls to roll five-of-a-kind.".format(n))

if __name__ == "__main__": main()
