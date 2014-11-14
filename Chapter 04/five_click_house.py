# five_click_house.py

from graphics import *

def main():
    # Create a graphics window
    win = GraphWin('Five Click House', 600, 500)
    win.setBackground('white')

    # Code to create objects with user clicks
    
    # Base of the house
    text = Text(Point(300, 15), 'This program will create a house with user mouse input. Click for further instructions.')
    text.draw(win)
    win.getMouse()
    text.setText('Click where the lower left corner will be, and then click where the upper right corner will be.')
    
    bp1 = win.getMouse()
    bp1.draw(win)
    bp2 = win.getMouse()
    bp2.draw(win)
    base = Rectangle(bp1, bp2)
    base.setFill('cyan')
    base.draw(win)
    bp1.undraw()
    bp2.undraw()

    # Door
    text.setText('Click in the house where you want the top center of the door to be.')

    dp = win.getMouse()
    dp0 = (bp2.getX()-bp1.getX()) / 10
    dp1 = Point((dp.getX()-dp0), (dp.getY()))
    dp2  = Point((dp.getX()+dp0), (bp1.getY()))
    door = Rectangle(dp1, dp2)
    door.setOutline('orange')
    door.setFill('black')
    door.draw(win)

    # Window
    text.setText('Click in the house where you want the window to be.')

    wp = win.getMouse()
    wp1 = Point((wp.getX()-dp0), (wp.getY()-dp0))
    wp2 = Point((wp.getX()+dp0), (wp.getY()+dp0))
    window = Rectangle(wp1, wp2)
    window.setOutline('orange')
    window.setFill('black')
    window.draw(win)
    l1 = Line(Point((wp.getX()-dp0), (wp.getY())), Point((wp.getX()+dp0), (wp.getY())))
    l1.setFill('orange')
    l1.draw(win)
    l2 = Line(Point((wp.getX()), (wp.getY()-dp0)), Point((wp.getX()), (wp.getY()+dp0)))
    l2.setFill('orange')
    l2.draw(win)

    # Roof
    text.setText('Click above the base of the house where you want the tip of the roof to be.') 

    rp = win.getMouse()
    roof = Polygon(Point((rp.getX()), (rp.getY())), Point((bp1.getX()), (bp2.getY())), Point((bp2.getX()), (bp2.getY())))
    roof.setFill('red')
    roof.draw(win)

    # Exit program
    text.setText('Click anywhere to exit')
    win.getMouse()
    win.close()

main()
