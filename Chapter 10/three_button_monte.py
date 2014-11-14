# three_button_monte.py

from graphics import *
from random import randrange
from button import Button

class Score:
    def __init__(self, window, x, y):
        self.score_wins = 0
        self.score_loses = 0
        self.win = window
        self.x = x
        self.y = y
    
    def display_score(self):
        self.wins = Text(Point(self.x+.03,self.y+.2), " Wins: {:>6}".format(self.score_wins))
        self.wins.setTextColor("white")
        self.wins.setStyle("bold")
        self.wins.draw(self.win)
        self.loses = Text(Point(self.x, self.y), "Loses: {:>6}".format(self.score_loses))
        self.loses.setTextColor("white")
        self.loses.setStyle("bold")
        self.loses.draw(self.win)

    def update_score(self):
        self.wins.undraw()
        self.loses.undraw()
        self.display_score()

    def won(self):
        self.score_wins += 1

    def lost(self):
        self.score_loses += 1

    def reset_score(self):
        self.score_wins = 0
        self.score_loses = 0

def main():
    # Create a graphics window
    win = GraphWin("Three Button Monte", 500, 500)
    win.setCoords(0, 0, 6, 5)
    win.setBackground("black")

    # Create and display a score object
    score = Score(win, .45, 4.6)
    score.display_score()

    door1 = Button(win, Point(1,2.5), 1.5, 2, "One")
    door1.activate()
    door2 = Button(win, Point(3,2.5), 1.5, 2, "Two")
    door2.activate()
    door3 = Button(win, Point(5,2.5), 1.5, 2, "Three")
    door3.activate()

    quitButton = Button(win, Point(5.5,.5), .5, .25, "Quit")
    
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        winner = randrange(3)
        if door1.clicked(pt) and winner == 0 or door2.clicked(pt) and winner == 1 or door3.clicked(pt) and winner == 2:
            score.won()
        else:
            if door1.clicked(pt) and winner != 0 or door2.clicked(pt) and winner != 1 or door3.clicked(pt) and winner != 2:
                score.lost()

        score.update_score()
        quitButton.activate()
        pt = win.getMouse()

if __name__ == "__main__": main()


