"""
File: my_drawing.py
Name: Elaine Chen 陳昭邑
----------------------
TODO: to draw a meme
"""

from campy.graphics.gobjects import GOval, GLine, GArc, GRect
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: to draw a picture
    """
    window = GWindow(width=600, height=500, title='Color Blind Test')
    number(window)


def number(window):
    face = GOval(150, 150)
    window.add(face, 250, 70)
    body1 = GLine(310, 200, 320, 300)
    window.add(body1)
    body2 = GLine(320, 300, 350, 400)
    window.add(body2)
    rhand1 = GLine(310, 200, 220, 240)
    window.add(rhand1)
    rhand2 = GLine(220, 240, 170, 320)
    window.add(rhand2)
    rfinger11 = GLine(170, 320, 160, 335)
    window.add(rfinger11)
    rfinger12 = GLine(160, 335, 160, 345)
    window.add(rfinger12)
    rfinger21 = GLine(170, 320, 167, 335)
    window.add(rfinger21)
    rfinger22 = GLine(167, 335, 172, 345)
    window.add(rfinger22)
    rfinger31 = GLine(170, 320, 175, 333)
    window.add(rfinger31)
    rfinger32 = GLine(175, 333, 182, 340)
    window.add(rfinger32)
    rfinger41 = GLine(170, 320, 185, 326)
    window.add(rfinger41)
    rfinger42 = GLine(185, 326, 190, 336)
    window.add(rfinger42)
    lhand1 = GLine(310, 200, 370, 260)
    window.add(lhand1)
    lhand2 = GLine(370, 260, 450, 280)
    window.add(lhand2)
    lfinger11 = GLine(450, 280, 455, 302)
    window.add(lfinger11)
    lfinger21 = GLine(450, 280, 450, 302)
    window.add(lfinger21)
    lfinger31 = GLine(448, 280, 445, 302)
    window.add(lfinger31)
    reye1 = GLine(270, 103, 320, 103)
    window.add(reye1)
    reye2 = GArc(50, 50, 180, 180, x=270, y=90)
    window.add(reye2)
    leye1 = GLine(340, 103, 380, 103)
    window.add(leye1)
    leye2 = GArc(40, 50, 180, 180, x=340, y=90)
    window.add(leye2)
    reyeball = GOval(6, 6)
    reyeball.filled = True
    window.add(reyeball, 300, 103)
    leyeball = GOval(6, 6)
    leyeball.filled = True
    window.add(leyeball, 360, 103)
    reyebrow = GLine(320, 98, 290, 85)
    window.add(reyebrow)
    frown = GLine(330, 98, 329, 93)
    window.add(frown)
    leyebrow = GLine(340, 98, 370, 85)
    window.add(leyebrow)
    mouth = GArc(100, 70, 0, 180, x=280, y=130)
    window.add(mouth)
    mouth1 = GArc(15, 7, 0, 180, x=330, y=140)
    window.add(mouth1)
    mouth2 = GArc(15, 7, 110, 180, x=270, y=145)
    window.add(mouth2)
    frame = GRect(400, 350)
    window.add(frame, 100, 50)


if __name__ == '__main__':
    main()
