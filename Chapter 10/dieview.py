# dieview.py
from graphics import *
from random import randrange

class DieView:
    """DieView is a widget that displays a graphical representation
    of a standard six-sided die."""

    def __init__(self, win, center, size):
        """Create a view of a die, e.g.:
        d1 = DieView(mywin, Point(40,50), 20)
        creates a die centered at (40,50) having sides
        of length 20."""

        # First define some standard values
        self.win = win
        self.background = 'white'
        self.foreground = 'black'
        self.psize = 0.1 * size
        hsize = size/2.0
        offset = 0.6 * hsize

        # Create a square for the face
        cx,cy = center.getX(), center.getY()
        p1 = Point(cx-hsize, cy-hsize)
        p2 = Point(cx+hsize, cy+hsize)
        rect = Rectangle(p1,p2)
        rect.draw(win)
        rect.setFill(self.background)

        # Create 7 circles for standard pip locations
        self.pips = [
                    self.__makePip(cx-offset, cy-offset)
                    self.__makePip(cx-offset, cy)
                    self.__makePip(cx-offset, cy+offset)
                    self.__makePip(cx,cy)
                    self.__makePip(cx+offset, cy-offset)
                    self.__makePip(cx+offset, cy)
                    self.__makePip(cx+offset, cy+offset)
                    ]

        self.onTable = [[], [3], [2,4], [2,3,4], [0,2,4,6], [0,2,3,4,6], [0,1,2,4,5,6]]

        # Draw an initial value
        self.setValue(1)

    def __makePip(self, x, y):
        "Internal helper method to draw a pip at (x,y)"
        pip = Circle(Point(x,y), self.psize)
        pip.setFill(self.background)
        pip.setOutline(self.background)
        pip.draw(self.win)
        return pip

    def setColor(self, color):
        self.foreground = color

    def setValue(self, value):
        "set this die to display value."
        # Turn all pips off
        for pip in self.pips:
            pip.setFill(self.background)

        # Turn the appropriate pips back on
        for i in self.onTable[value]:
            self.pips[i].setFill(self.foreground)
