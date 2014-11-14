# main.py

from graphics import *
import winterScene
import five_click_house
import snowman

def main():
    # Create a graphics window
    win = winterScene.winterScene()

    # Create a house
    five_click_house.house(win)

    # Create a snowman
    snowman.snowman(win)

    # Pause for mouse click, then close program
    win.getMouse()
    win.close()

if __name__=='__main__':
    main()
