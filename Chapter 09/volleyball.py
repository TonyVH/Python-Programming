# volleyball.py

import random

def main():
    printIntro()
    probA, probB, n = getInputs()
    winsA, winsB = simNGames(probA, probB, n)
    printSummary(winsA, winsB)

def printIntro():
    print("This program will simulate a volleyball game.")
    print("The two teams will be represented be teamA and teamB.")
    print("The skill levels of each team will be represented by")
    print("a decimal point number between 0 and 1. Games will be played")
    print("to 15, but must also be won by 2 points.\n")

def getInputs():
    probA = float(input("What is the probability team A wins the rally? "))
    probB = float(input("What is the probability team B wins the rally? "))
    n = int(input("How many games should be played? "))
    return probA, probB, n

def simNGames(probA, probB, n):
    winsA = 0
    winsB = 0

    for i in range(n):
        scoreA, scoreB = simOneGame(probA, probB, i)
        if scoreA > scoreB:
            winsA += 1
        else:
            winsB +=1
    return winsA, winsB

def simOneGame(probA, probB):
    scoreA = 0
    scoreB = 0

    if i % 2 == 0:
        serving = "A"
    else:
        serving = "B"

    while not gameOver(scoreA, scoreB):
        if serving == "A":
            if random.random() < probA:
                scoreA += 1
            else:
                serving = "B"
        else:
            if random.random() < probB:
                scoreB += 1
            else:
                serving = "A"
    return scoreA, scoreB

def gameOver(a, b):
    return a == 15 and a-b >= 2 or b == 15 and b-a >= 2

def printSummary(winsA, winsB):
    n = winsA + winsB
    print("Number of games simulated: {}".format(n))
    print("Wins for team A: {0} {1:0.2%}".format(winsA, winsA/n))
    print("wins for team B: {0} {1:0.2%}".format(winsB, winsB/n))

if __name__ == "__main__": main()
