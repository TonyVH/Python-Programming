# button.py
from graphics import *

class Button:
    """A button is a labeled rectangle in a window.
    It is activated or deactivated with the activate()
    and deactivate() methods. The clicked(p) method
    returns true if the button is active and p is inside it."""

    def __init__(self, win, center, radius, label):
        """Creates a rectangular button, eg:
        qb = Button(myWIn, centerPoint, width, height, "Quit")"""

        self.center = center
        self.radius = radius 
        self.circ = Circle(self.center,self.radius)
        self.circ.setFill("lightgrey")
        self.circ.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

        self.xmax, self.xmin = self.circ.getP2().getX(), self.circ.getP1().getX()    # X/Y min and max values based on
        self.ymax, self.ymin = self.circ.getP2().getY(), self.circ.getP1().getY()    # the square box containing the circle

    def clicked(self, p):
        "returns true if button active and p is inside"
        return (self.active and
                self.xmin <= p.getX() <= self.xmax and
                self.ymin <= p.getY() <= self.ymax)

    def getLabel(self):
        "Returns the label string of this button."
        return self.label.getText()

    def activate(self):
        "Sets this button to 'active'."
        self.label.setFill("black")
        self.circ.setWidth(2)
        self.active = True

    def deactivate(self):
        "Sets this button to 'inactive'."
        self.label.setFill("darkgrey")
        self.circ.setWidth(1)
        self.active = False
