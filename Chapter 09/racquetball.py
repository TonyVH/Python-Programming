# racquetball_.py

import random

def main():
    printIntro()
    probA, probB, n, m = getInputs()
    winsA, winsB, shutoutsA, shutoutsB = simMMatches(probA, probB, n, m)
    printSummary(winsA, winsB, shutoutsA, shutoutsB)

def printIntro():
    print('This program simulates a game of racquetball between two')
    print('players called "A" and "B". The abilities of each player is')
    print('indicated by a probablity (a number between 0 and 1) that')
    print('the player wins the point when serving. Player A always')
    print('has the first serve.')

def getInputs():
    # Returns the three simulation parameters probA, probB, and n
    a = float(input('What is the probability player A wins a serve? '))
    b = float(input('What is the probability player B wins a serve? '))
    n = int(input('How many games should be played per match (e.g. best of 7)? '))
    m = int(input('How many matches to play? ')) 
    return a, b, n, m

def simMMatches(probA, probB, n, m):
    winsA = 0
    winsB = 0
    outA = 0
    outB = 0
    for i in range(m):
        gamesA, gamesB, shutoutsA, shutoutsB = simNGames(probA, probB, n)
        if gamesA > gamesB:
            winsA += 1
        else:
            winsB += 1

        if shutoutsA > 0:
            outA += shutoutsA
        else:
            if shutoutsB > 0:
                outB += shutoutsB

    return winsA, winsB, outA, outB

def simNGames(probA, probB, n):
    # Simulate n games and returns winsA and winsB
    gamesA = 0
    gamesB = 0
    shutoutsA = 0
    shutoutsB = 0
    for i in range(n):
        scoreA, scoreB, shutoutA, shutoutB = simOneGame(probA, probB, i)
        if scoreA > scoreB:
            gamesA += 1
        else:
            gamesB += 1

        if shutoutA == 1:
            shutoutsA += 1
        else:
            if shutoutB == 1:
                shutoutsB += 1

    return gamesA, gamesB, shutoutsA, shutoutsB

def simOneGame(probA, probB, i):
    # Score for each game
    scoreA = 0
    scoreB = 0
    # Alternate who serves first then begin the game loop
    if i % 2 == 0:
        serving = 'A'
    else:
        serving = 'B'
    while not gameOver(scoreA, scoreB):
        if serving == 'A':
            if random.random() < probA:
                scoreA += 1
            else:
                serving = 'B'
        else:
            if random.random() < probB:
                scoreB += 1
            else:
                serving = 'A'

    shutoutA = 0
    shutoutB = 0
    if scoreA == 7 and scoreB == 0:
        shutoutA = 1
    elif scoreB == 7 and scoreA == 0:
        shutoutB = 1

    return scoreA, scoreB, shutoutA, shutoutB

def gameOver(a,b):
    # a and b represent scores for a racquetball game
    # Returns True if the game is over, False otherwise
    return a == 15 or b == 15 or a == 7 and b == 0 or a == 0 and b == 7

def printSummary(winsA, winsB, shutoutsA, shutoutsB):
    # Prints a summary of wins for each player
    n = winsA + winsB
    print('\nMatches simulated:', n)
    print('Wins for A: {0} ({1:0.1%})'.format(winsA, winsA/n))
    if shutoutsA > 0:
        print('Shutouts for A: {0}'.format(shutoutsA))
    print('Wins for B: {0} ({1:0.1%})'.format(winsB, winsB/n))
    if shutoutsB > 0:
        print('Shutouts for B: {0}'.format(shutoutsB))

if __name__=='__main__':
    main()
