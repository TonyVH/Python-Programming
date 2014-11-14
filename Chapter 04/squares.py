# squares.py

from graphics import *

def main():
    win = GraphWin()
    shape = Rectangle(Point(30, 30), Point(50, 50))
    shape.setOutline('red')
    shape.setFill('red')
    shape.draw(win)
    text = Text(Point(100, 10), 'Click to move the square.')
    text.draw(win)

    for i in range(10):
        p = win.getMouse()
        c = shape.getCenter()
        dx = p.getX() - c.getX()
        dy = p.getY() - c.getY()
        shape.move(dx,dy)
    text.setText('Click anywhere to exit')
    win.getMouse()
    win.close()

main()
