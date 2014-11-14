# face.py

from graphics import *

win = GraphWin()

center = Point(100,100)
radius = 30

head = Circle(center, radius)
left_eye = Circle(Point(center.getX()-radius/2, center.getY()-radius/2), radius/8)
right_eye = left_eye.clone()
right_eye.move(radius, 0)
nose = Circle(center, radius/7)
mouth = Oval(Point(center.getX()-radius/2, center.getY()+radius/2), Point(center.getX()+radius/2, center.getY()+radius/1.5))

head.draw(win)
left_eye.draw(win)
right_eye.draw(win)
nose.draw(win)
mouth.draw(win)

win.getMouse()
win.close()