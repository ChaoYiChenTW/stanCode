"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from campy.graphics.gobjects import GLabel
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 1000 / 120 # 120 frames per second
# FRAME_RATE = 50
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add animation loop here!
    vx = graphics.get_vx()
    vy = graphics.get_vy()
    wait_game_start(graphics)

    life = NUM_LIVES
    score = 0

    while True:
        graphics.ball.move(vx, vy)
        if graphics.ball.x+graphics.ball.width >= graphics.window.width or graphics.ball.x <= 0:
            vx = -vx
        if graphics.ball.y + graphics.ball.height <= 0:
            vy = -vy
        if is_touching_object(graphics):
            something = is_touching_object(graphics)
            # bricks
            if something.y < graphics.paddle.y:
                graphics.window.remove(something)
                score += 1
                graphics.scoreboard.text = 'Scores: ' + str(score)
                vy = -vy
            # paddle
            elif graphics.ball.y + graphics.ball.height <= graphics.paddle.y + 5:
                vy = -abs(vy)
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            graphics = BreakoutGraphics()
            vx = graphics.get_vx()
            vy = graphics.get_vy()
            wait_game_start(graphics)
            life -= 1
            if life == 0:
                result = 'lose'
                break

        num_brick = graphics.get_brick_rows()*graphics.get_brick_cols()
        if score == num_brick:
            result = 'win'
            break

        pause(FRAME_RATE)
    if result == 'lose':
        game_over(graphics)
    elif result == 'win':
        game_win(graphics)


def wait_game_start(graphics):
    while True:
        if graphics.get_start():
            break
        pause(FRAME_RATE)


def is_touching_object(graphics):
    if graphics.window.get_object_at(graphics.ball.x, graphics.ball.y):
        return graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
    elif graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y):
        return graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y)
    elif graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height):
        return graphics.window.get_object_at(graphics.ball.x, graphics.ball.y+graphics.ball.height)
    elif graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height):
        return graphics.window.get_object_at(graphics.ball.x+graphics.ball.width, graphics.ball.y+graphics.ball.height)


def game_over(graphics):
    graphics.window.add(graphics.gameover, x=0, y=300)
    move_vx = 5
    while True:
        graphics.gameover.move(move_vx, 0)
        if graphics.gameover.x < 0 or graphics.gameover.x + graphics.gameover.width > graphics.window.width:
            move_vx = -move_vx
        pause(FRAME_RATE)


def game_win(graphics):
    graphics.window.add(graphics.gamewin, x=0, y=300)
    move_vx = 5
    while True:
        graphics.gamewin.move(move_vx, 0)
        if graphics.gamewin.x < 0 or graphics.gamewin.x + graphics.gamewin.width > graphics.window.width:
            move_vx = -move_vx
        pause(FRAME_RATE)


if __name__ == '__main__':
    main()
