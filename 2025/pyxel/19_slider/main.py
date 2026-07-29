# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 128, 128

START_R = 7
START_C = 8

MODE_TITLE     = "title"
MODE_PLAY      = "play"
MODE_GAME_OVER = "game_over"

CAMERA_PAD_X   = 0
CAMERA_LIMIT_L = -W
CAMERA_LIMIT_R = W

# Game
class Game:
    def __init__(self):
        """ Constructor """

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        # Tilemap(Copy 0 -> 1)
        pyxel.tilemaps[1].blt(0, 0, 0, 0, 0, 640, 128)

        # Score
        self.score = 0

        # Camera
        self.camera_x = 0

        # Player
        self.player = sprite.PlayerSprite(
            START_C * 8, START_R * 8, 16, 0)

        # Run
        pyxel.run(self.update, self.draw)

    def update(self):

        # Controll
        self.controll()

        # Player
        self.player.update()

    def draw(self):
        pyxel.cls(1)

        # Camera(on)
        self.camera_on()

        # Tilemap
        pyxel.bltm(0, 0, 0, 0, 0, 640, 128, 0)

        # Player
        self.player.draw()

        # Camera(off)
        self.camera_off()

        # Message
        # if self.game_mode == MODE_TITLE:
        #     msg = "WASD TO PLAY"
        #     pyxel.text(W/2-len(msg)*2, 16, msg, 7)
        # elif self.game_mode == MODE_GAME_OVER:
        #     msg = "GAME OVER"
        #     pyxel.text(W/2-len(msg)*2, 16, msg, 7)

        # Score
        pyxel.text(1, 1, 
            "SCORE:{:04}".format(self.score), 7)

    def reset(self):

        # Tilemap(1 -> 0)
        pyxel.tilemaps[0].blt(0, 0, 1, 0, 0, 640, 128) # Copy

        # Camera
        self.camera_x = 0

        # Reset
        self.player.reset(START_X, START_Y)

    def controll(self):
        # Player
        if pyxel.btnp(pyxel.KEY_W):
            self.player.go_up()
        if pyxel.btnp(pyxel.KEY_A):
            self.player.go_left()
        if pyxel.btnp(pyxel.KEY_S):
            self.player.go_down()
        if pyxel.btnr(pyxel.KEY_D):
            self.player.go_right()

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