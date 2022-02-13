"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10        # Number of rows of bricks.
BRICK_COLS = 10        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius = BALL_RADIUS, paddle_width = PADDLE_WIDTH,
                 paddle_height = PADDLE_HEIGHT, paddle_offset = PADDLE_OFFSET,
                 brick_rows = BRICK_ROWS, brick_cols = BRICK_COLS,
                 brick_width = BRICK_WIDTH, brick_height = BRICK_HEIGHT,
                 brick_offset = BRICK_OFFSET, brick_spacing = BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(PADDLE_WIDTH, PADDLE_HEIGHT)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width-self.paddle.width)/2, y=self.window.height-PADDLE_OFFSET)
        # Center a filled ball in the graphical window
        self.ball = GOval(BALL_RADIUS, BALL_RADIUS)
        self.ball.filled = True
        self.window.add(self.ball, x=(self.window.width-self.ball.width)/2, y=(self.window.height-self.ball.height)/2)
        # Create a scoreboard
        self.scoreboard = GLabel('Scores: 0', 100, 10)
        self.scoreboard.font = '-30'
        self.window.add(self.scoreboard, x=0, y=self.window.height)
        # Default initial velocity for the ball
        self.__dy = INITIAL_Y_SPEED
        self.__dx = random.randint(1, MAX_X_SPEED)
        # Initialize our mouse listeners
        self.__game_start = 2 < 1
        onmouseclicked(self.start)
        onmousemoved(self.move_paddle)

        # Draw bricks
        for i in range(BRICK_COLS):
            for j in range(BRICK_ROWS):
                brick_x = (BRICK_WIDTH+BRICK_SPACING) * i
                brick_y = BRICK_OFFSET + (BRICK_HEIGHT+BRICK_SPACING) * j
                self.brick = GRect(BRICK_WIDTH, BRICK_HEIGHT)
                self.brick.filled = True
                if j <= 1:
                    color = 'red'
                elif j <= 3:
                    color = 'orange'
                elif j <= 5:
                    color = 'yellow'
                elif j <= 7:
                    color = 'green'
                else:
                    color = 'blue'
                self.brick.color = color
                self.brick.fill_color = color
                self.window.add(self.brick, x=brick_x, y=brick_y)

        self.gameover = GLabel('Game Over', 100, 100)
        self.gameover.font = '-40'
        self.gamewin = GLabel('You Win', 100, 100)
        self.gamewin.font = '-40'

    def move_paddle(self, event):
        self.window.add(self.paddle, x=event.x-self.paddle.width/2, y=self.window.height-PADDLE_OFFSET)
        if event.x >= self.window.width-self.paddle.width/2:
            self.window.add(self.paddle, x=self.window.width-self.paddle.width, y=self.window.height-PADDLE_OFFSET)
        elif event.x <= self.paddle.width/2:
            self.window.add(self.paddle, x=0, y=self.window.height-PADDLE_OFFSET)

    def start(self, event):
        self.__game_start = 2 > 1

    def get_start(self):
        return self.__game_start

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    @staticmethod
    def get_brick_rows():
        return BRICK_ROWS

    @staticmethod
    def get_brick_cols():
        return BRICK_COLS
