# snowman.py

from graphics import *

def snowman(window):
    bodyCenter = window.getMouse()
    center = Point(bodyCenter.getX(), bodyCenter.getY())
    radius = 50
    mid = Circle(center, radius)
    mid.setFill('white')
    bottom = Circle(Point(bodyCenter.getX(), bodyCenter.getY()+(radius*2)), radius*1.5)
    bottom.setFill('white')
    top = Circle(Point(bodyCenter.getX(), bodyCenter.getY()-(radius*1.5)), radius*0.75)
    top.setFill('white')

    bottom.draw(window)
    mid.draw(window)
    top.draw(window)

    # Arms and fingers
    leftArm = Line(Point(center.getX()-45, center.getY()), Point(center.getX()-85, center.getY()-30))
    leftArm.setWidth(3)
    leftFinger1 = Line(Point(center.getX()-85, center.getY()-30), Point(center.getX()-90, center.getY()-40))
    leftFinger1.setWidth(2)
    leftFinger2 = Line(Point(center.getX()-85, center.getY()-30), Point(center.getX()-83, center.getY()-40))
    leftFinger2.setWidth(2)
    leftFinger3 = Line(Point(center.getX()-85, center.getY()-30), Point(center.getX()-75, center.getY()-40))
    leftFinger3.setWidth(2)
    rightArm = Line(Point(center.getX()+45, center.getY()), Point(center.getX()+80, center.getY()+45))
    rightArm.setWidth(3)
    rightFinger1 = Line(Point(center.getX()+80, center.getY()+45), Point(center.getX()+75, center.getY()+55))
    rightFinger1.setWidth(2)
    rightFinger2 = Line(Point(center.getX()+80, center.getY()+45), Point(center.getX()+83, center.getY()+55))
    rightFinger2.setWidth(2)
    rightFinger3 = Line(Point(center.getX()+80, center.getY()+45), Point(center.getX()+90, center.getY()+55))
    rightFinger3.setWidth(2)
    
    leftArm.draw(window)
    rightArm.draw(window)
    leftFinger1.draw(window)
    leftFinger2.draw(window)
    leftFinger3.draw(window)
    rightFinger1.draw(window)
    rightFinger2.draw(window)
    rightFinger3.draw(window)

    # Eyes
    eyeCenter = window.getMouse()
    eye1 = Circle(eyeCenter, 7)
    eye1.setFill('black')
    eye2 = eye1.clone()
    eye2.move(25, 0)

    eye1.draw(window)
    eye2.draw(window)

    # Mouth
    mouthCenter = window.getMouse()
    mouth1 = Circle(mouthCenter, 4)
    mouth1.setFill('black')
    mouth2 = mouth1.clone()
    mouth2.move(6, -1)
    mouth3 = mouth1.clone()
    mouth3.move(-6, -1)
    mouth4 = mouth1.clone()
    mouth4.move(12, -4)
    mouth5 = mouth1.clone()
    mouth5.move(-12, -4)

    mouth1.draw(window)
    mouth2.draw(window)
    mouth3.draw(window)
    mouth4.draw(window)
    mouth5.draw(window)

    # Nose
    nosePoint1 = window.getMouse()
    nosePoint2 = window.getMouse()
    nosePoint3 = window.getMouse()
    nose = Polygon(nosePoint1, nosePoint2, nosePoint3)
    nose.setFill('orange')

    nose.draw(window)
