# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

W, H = 128, 128

CAMERA_PAD_X   = 0
CAMERA_LIMIT_L = -W
CAMERA_LIMIT_R = W

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ Constructor """
        self.x    = x
        self.y    = y
        self.u    = u
        self.v    = v
        self.w    = w
        self.h    = h
        self.vx   = 0
        self.vy   = 0

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 
            self.u, self.v,
            self.w, self.h, 0)

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
        pyxel.init(W, H, title="Hello, Pyxel!!", fps=50)
        pyxel.load("my_resource.pyxres")

        # Score
        self.score = 0

        # Camera
        self.camera_x = 0

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

        # Camera(on)
        self.camera_on()

        # Player
        self.player.draw()

        # Camera(off)
        self.camera_off()

        # Score
        pyxel.text(1, 1, 
            "SCORE:{:03}".format(self.score), 7)

    def controll(self):
        # Btn
        if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
            print("pressed!!")

    def camera_on(self):
        line_r = W - self.camera_x - CAMERA_PAD_X
        if line_r < self.player.x:
            self.camera_x += line_r - self.player.x
            if self.camera_x < CAMERA_LIMIT_L:
                self.camera_x = CAMERA_LIMIT_L
        line_l = 0 - self.camera_x + CAMERA_PAD_X
        if self.player.x < line_l:
            self.camera_x += line_l - self.player.x
            if CAMERA_LIMIT_R < self.camera_x:
                self.camera_x = CAMERA_LIMIT_R
        pyxel.camera(-self.camera_x, 0)

    def camera_off(self):
        pyxel.camera()

def main():
    """ Main """
    Game()

if __name__ == "__main__":
    main()