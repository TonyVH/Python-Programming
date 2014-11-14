# futval_graph2.py

from graphics import *

def main():
    # Introduction
    print('This program plots the growth of a 10 year investment.')

    # Get principal and interest rate
    principal = eval(input('Enter the initial principal: '))
    apr = eval(input('Enter the annualized interest rate: '))

    # Create a graphics window with labels on left edge and lines going accross
    win = GraphWin('Investment Growth Chart', 640, 480)
    win.setBackground('white')
    win.setCoords(-1.75, -200, 11.5, 10400)
    Text(Point(-1, 0), ' 0.0K').draw(win)
    Text(Point(-1, 2500), ' 2.5K').draw(win)
    Text(Point(-1, 5000), ' 5.0K').draw(win)
    Text(Point(-1, 7500), ' 7.5K').draw(win)
    Text(Point(-1, 10000), '10.0K').draw(win)
    Line(Point(-0.5, 0), Point(10, 0)).draw(win)
    Line(Point(-0.5, 2500), Point(11, 2500)).draw(win)
    Line(Point(-0.5, 5000), Point(11, 5000)).draw(win)
    Line(Point(-0.5, 7500), Point(11, 7500)).draw(win)
    Line(Point(-0.5, 10000), Point(11, 10000)).draw(win)
    
    # Draw bar for initial principal
    bar = Rectangle(Point(0, 0), Point(1, principal))
    bar.setFill('green')
    bar.setWidth(2)
    bar.draw(win)

    # Draw a bar for each subsequent year
    for year in range(1,11):
        principal = principal * (1+apr)
        bar = Rectangle(Point(year, 0), Point(year+1, principal))
        bar.setFill('green')
        bar.setWidth(2)
        bar.draw(win)

    input('Press <Enter> to quit')
    win.close()

main()
