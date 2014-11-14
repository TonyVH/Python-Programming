# snowman.py

from graphics import *

def winterScene():
    window = GraphWin('Winter Scene', 1200, 600)
    # Sky
    sky = Rectangle(Point(0, 0), Point(1200, 350))
    sky.setFill(color_rgb(0, 0, 200))
    sky.draw(window)

    # Ground
    ground = Rectangle(Point(0, 350), Point(1200, 600))
    ground.setFill('white')
    ground.draw(window)

    # Lake with ice skater
    lake = Oval(Point(90, 435), Point(340, 400))
    lake.setFill(color_rgb(0, 0, 250))
    lake.draw(window)

    # Tree
    treeBase = Rectangle(Point(100, 400), Point(150, 475))
    treeBase.setFill('brown')
    treeBase.draw(window)
    treeTop = Polygon(Point(25, 400), Point(225, 400), Point(125, 150))
    treeTop.setFill(color_rgb(0, 50, 0))
    treeTop.draw(window)

    # Sun
    sun = Circle(Point(1200, 0), 75)
    sun.setFill('yellow')
    sun.draw(window)

    return window
