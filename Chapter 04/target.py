# target.py
# This program will create a target

from graphics import *

def main():
    # Create a graphics window
    win = GraphWin('Target', 400, 400)
    win.setBackground('white')

    # Create circles that make up the target
    center = Point(200, 200)
    radius = 25

    circ1 = Circle(center, radius)
    circ1.setFill('yellow')

    circ2 = Circle(center, radius*2)
    circ2.setFill('red')

    circ3 = Circle(center, radius*3)
    circ3.setFill('blue')

    circ4 = Circle(center, radius*4)
    circ4.setFill('black')

    circ5 = Circle(center, radius*5)
    circ5.setFill('white')

    circ5.draw(win)
    circ4.draw(win)
    circ3.draw(win)
    circ2.draw(win)
    circ1.draw(win)

    # Close the window after user mouse click
    win.getMouse()
    win.close()

main()
