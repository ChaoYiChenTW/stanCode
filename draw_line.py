"""
File: draw_line.py
Name: Elaine Chen 陳昭邑
-------------------------
TODO: draw lines and circles while mouse clicking
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

SIZE = 10

window = GWindow()
numClick = 0
originX = 0
originY = 0


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global numClick, originX, originY
    numClick += 1
    print(numClick)
    if numClick == 1:  # draw a circle
        circle = GOval(SIZE, SIZE)
        window.add(circle, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        originX = mouse.x
        originY = mouse.y
    else:  # remove a circle and draw a line
        obj = window.get_object_at(originX, originY)
        window.remove(obj) 
        line = GLine(originX, originY, mouse.x, mouse.y)
        window.add(line)
        numClick = 0


if __name__ == "__main__":
    main()
