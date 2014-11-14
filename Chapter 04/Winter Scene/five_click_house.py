# five_click_house.py

from graphics import *

def house(window):
    # Base of the house
    bp1 = window.getMouse()
    bp1.draw(window)
    bp2 = window.getMouse()
    bp2.draw(window)
    base = Rectangle(bp1, bp2)
    base.setFill('cyan')
    base.draw(window)
    bp1.undraw()
    bp2.undraw()

    # Door
    dp = window.getMouse()
    dp0 = (bp2.getX()-bp1.getX()) / 10
    dp1 = Point((dp.getX()-dp0), (dp.getY()))
    dp2  = Point((dp.getX()+dp0), (bp1.getY()))
    door = Rectangle(dp1, dp2)
    door.setOutline('orange')
    door.setFill('black')
    door.draw(window)

    # Window
    wp = window.getMouse()
    wp1 = Point((wp.getX()-dp0), (wp.getY()-dp0))
    wp2 = Point((wp.getX()+dp0), (wp.getY()+dp0))
    win = Rectangle(wp1, wp2)
    win.setOutline('orange')
    win.setFill('black')
    win.draw(window)
    l1 = Line(Point((wp.getX()-dp0), (wp.getY())), Point((wp.getX()+dp0), (wp.getY())))
    l1.setFill('orange')
    l1.draw(window)
    l2 = Line(Point((wp.getX()), (wp.getY()-dp0)), Point((wp.getX()), (wp.getY()+dp0)))
    l2.setFill('orange')
    l2.draw(window)

    # Roof
    rp = window.getMouse()
    roof = Polygon(Point((rp.getX()), (rp.getY())), Point((bp1.getX()), (bp2.getY())), Point((bp2.getX()), (bp2.getY())))
    roof.setFill('red')
    roof.draw(window)

