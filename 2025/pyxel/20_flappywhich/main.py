# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

W, H = 128, 128

VEL_X     = 0.8
VEL_Y     = 0.8
GRAVITY_X = -0.01
GRAVITY_Y = 0.02

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ Constructor """
        self.x  = x
        self.y  = y
        self.u  = u
        self.v  = v
        self.w  = w
        self.h  = h
        self.vx = 0
        self.vy = -VEL_Y
        self.accel_flg = False

    def update(self):
        self.x += self.vx
        self.y += self.vy

        # Accel
        if self.accel_flg:
            self.vx = VEL_X
            self.vy = VEL_Y
        else:
            # Gravity
            self.vx += GRAVITY_X
            self.vy += GRAVITY_Y

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 
            self.u, self.v,
            self.w, self.h, 0)

    def action_press(self):
        self.accel_flg = True

    def action_release(self):
        self.accel_flg = False
        self.vx = 0
        self.vy = -VEL_Y


class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v)

    def update(self):
        super().update()

    def draw(self):
        super().draw()

# Game
class Game:
    def __init__(self):
        """ Constructor """

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!", fps=32)
        pyxel.load("my_resource.pyxres")

        # Score
        self.score = 0

        # Player
        self.player = PlayerSprite(
            20, H/2, 16, 0)

        # Run
        pyxel.run(self.update, self.draw)

    def update(self):

        # Controll
        self.controll()

        # Player
        self.player.update()

    def draw(self):

        # Clear
        pyxel.cls(0)

        # Player
        self.player.draw()

        # Score
        pyxel.text(1, 1, 
            "SCORE:{:03}".format(self.score), 7)

    def controll(self):
        # Btn
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            print("pressed!!")
            self.player.action_press()
        if pyxel.btnr(pyxel.MOUSE_BUTTON_LEFT):
            print("released!!")
            self.player.action_release()

def main():
    """ Main """
    Game()

if __name__ == "__main__":
    main()