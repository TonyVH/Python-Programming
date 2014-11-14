# changing_background.py

from graphics import *

def main():
    win = GraphWin()

    i = 5
    while True:
        for i in range(255):
            win.setBackground(color_rgb(i, 25, 90))

main()
