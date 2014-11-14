# roller.py
# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import *

from cbutton import Button
from dieview import DieView

def main():

    # Create the application window
    win = GraphWin('Dice Roller', 500, 500)
    win.setCoords(0, 0, 10, 10)
    win.setBackground(color_rgb(0,75,0))

    # Draw the interface widgets
    die1 = DieView(win, Point(3,7), 2)

    die2 = DieView(win, Point(7,7), 2)
    rollButton = Button(win, Point(5,4.5), 1.25, 'Roll Dice')
    rollButton.activate()
    quitButton = Button(win, Point(5,1), 1, 'Quit')

    # Event loop
    pt = win.getMouse()
    while not quitButton.clicked(pt):
        if rollButton.clicked(pt):
            value1 = randrange(1,7)
            #die1.setColor(color_rgb(randrange(255), randrange(255), randrange(255)))
            die1.setValue(value1)
            value2 = randrange(1,7)
            die2.setColor(color_rgb(randrange(255), randrange(255), randrange(255)))
            die2.setValue(value2)
            quitButton.activate()
        pt = win.getMouse()

    # Exit Program
    win.close()

if __name__ == '__main__': 
    main()
