# futval_graph.py

from graphics import *

def main():
    # Introduction
    print('This program plots the growth of a 10-year investment.')
    
    # Get Principle and APR
    principal = eval(input('Enter the initial principal: '))
    apr = eval(input('Enter the annualized interest rate: '))

    # Create a graphics window with labels on the left side
    win = GraphWin('Investment Growth Chart', 320, 240)
    win.setBackground('white')
    Text(Point(20, 230), ' 0.0K').draw(win)
    Text(Point(20, 180), ' 2.5K').draw(win)
    Text(Point(20, 130), ' 5.0K').draw(win)
    Text(Point(20, 80), ' 7.5K').draw(win)
    Text(Point(20, 30), '10.0K').draw(win)

    # Draw bar for initial principal
    height = principal * 0.02
    bar = Rectangle(Point(40, 230), Point(65, 230-height))
    bar.setFill('red')
    bar.setWidth(2)
    bar.draw(win)

    # Draw bars for successive years
    for year in range(1,11):
        # Calculate value for the next year
        principal = principal * (1+apr)
        # Draw bar for this value
        x11 = year*25 + 40
        height = principal * 0.02
        bar = Rectangle(Point(x11, 230), Point(x11+25, 230-height))
        bar.setFill('red')
        bar.setWidth(2)
        bar.draw(win)

    input('Press <Enter> to quit')
    win.close()

main()

