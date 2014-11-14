from graphics import *

def main():
    win = GraphWin('Graphics Test Window', 500, 500)
    circ = Circle(Point(250, 250), 20)
    circ.draw(win)
    
    win.getMouse()

    circ.move(0, 200)

    win.getMouse()

main()
