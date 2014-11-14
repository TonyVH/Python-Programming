from graphics import *

def main():
    # Create a graphics window
    win = GraphWin('Color Fill', 400, 400)
    win.setBackground('white')
    
    # Create a square
    p1 = Point(150, 150)
    p2 = Point(250, 250)
    rec = Rectangle(p1, p2)
    rec.draw(win)

    # Create color fill choice buttons
    r1 = Point(10, 10)
    r2 = Point(30, 30)
    red = Rectangle(r1, r2)
    red.setFill('red')
    red.draw(win)

    b1 = Point(10, 50)
    b2 = Point(30, 70)
    blue = Rectangle(b1, b2)
    blue.setFill('blue')
    blue.draw(win)

    o1 = Point(10, 90)
    o2 = Point(30, 110)
    orange = Rectangle(o1, o2)
    orange.setFill('orange')
    orange.draw(win)

    c1 = Point(10, 130)
    c2 = Point(30, 150)
    cyan = Rectangle(c1, c2)
    cyan.setFill('cyan')
    cyan.draw(win)

    g1 = Point(10, 170)
    g2 = Point(30, 190)
    green = Rectangle(g1, g2)
    green.setFill('green')
    green.draw(win)

    pu1 = Point(10, 210)
    pu2 = Point(30, 230)
    purple = Rectangle(pu1, pu2)
    purple.setFill('purple')
    purple.draw(win)

    bl1 = Point(10, 250)
    bl2 = Point(30, 270)
    black = Rectangle(bl1, bl2)
    black.setFill('black')
    black.draw(win)

    # Color selector
    def colorSelect():
        rec.setFill('white')
        color_select = win.getMouse()
        if color_select.getX() in range(r1.getX(), r2.getX()) and color_select.getY() in range(r1.getY(), r2.getY()):
            color = 'red'
        elif color_select.getX() in range(b1.getX(), b2.getX()) and color_select.getY() in range(b1.getY(), b2.getY()):
            color = 'blue'
        elif color_select.getX() in range(o1.getX(), o2.getX()) and color_select.getY() in range(o1.getY(), o2.getY()):
            color = 'orange'
        elif color_select.getX() in range(c1.getX(), c2.getX()) and color_select.getY() in range(c1.getY(), c2.getY()):
            color = 'cyan'
        elif color_select.getX() in range(g1.getX(), g2.getX()) and color_select.getY() in range(g1.getY(), g2.getY()):
            color = 'green'
        elif color_select.getX() in range(pu1.getX(), pu2.getX()) and color_select.getY() in range(pu1.getY(), pu2.getY()):
            color = 'purple'
        elif color_select.getX() in range(bl1.getX(), bl2.getX()) and color_select.getY() in range(bl1.getY(), bl2.getY()):
            color = 'black'
        else:
            colorSelect()

        # rec fill with chosen color
        button = win.getMouse()
        if button.getX() in range(p1.getX(), p2.getX()) and button.getY() in range(p1.getY(), p2.getY()):
            rec.setFill(color)
            text = Text(Point(200, 385), 'Click anywhere in the white space to start over')
            text.draw(win)
            win.getMouse()
            text.undraw()
        else:
            colorSelect()

    while True:
        colorSelect()

main()
