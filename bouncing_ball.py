"""
File: bouncing_ball.py
Name: Elaine Chen 陳昭邑
-------------------------
TODO: Make a ball fall freely when a mouse clicks. The ball could drop up to three times.
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40

window = GWindow(800, 500, title='bouncing_ball.py')
ball = GOval(SIZE, SIZE, x=START_X, y=START_Y)
count = 0  # how many times does the ball drop
running = False  # if the ball is falling


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    ball.filled = True
    window.add(ball)
    onmouseclicked(start)


def start(mouse):
    global running
    if running:  # don't bother the ball if it is falling
        return
    running = True
    global count
    count += 1
    if count > 3:
        return  # stop the ball from falling after dropping 3 times
    vy = 0  # initial velocity on y-axis
    while True:
        dy = 2*vy + GRAVITY/2
        if ball.y + dy >= window.height:
            ball.move(VX, window.height - ball.y)
            vy = -vy * REDUCE
        else:
            ball.move(VX, dy)
            vy += GRAVITY
        pause(DELAY)
        if ball.x >= window.width:
            break
    window.add(ball, x=START_X, y=START_Y)
    running = False


if __name__ == "__main__":
    main()
