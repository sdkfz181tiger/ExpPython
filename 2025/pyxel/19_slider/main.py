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

CAMERA_PAD_X   = 0
CAMERA_LIMIT_L = -W
CAMERA_LIMIT_R = W

TILE_NONE  = 0
TILE_COIN  = 1
TILE_BLOCK = 2

# u, v
TILE_COINS = {
    (0, 2): TILE_COIN
}

# u, v
TILE_BLOCKS = {
    (0, 4): TILE_BLOCK, (1, 4): TILE_BLOCK,
    (2, 4): TILE_BLOCK, (3, 4): TILE_BLOCK,
    (4, 4): TILE_BLOCK, (5, 4): TILE_BLOCK, 
    (6, 4): TILE_BLOCK, (7, 4): TILE_BLOCK,
    (0, 5): TILE_BLOCK, (1, 5): TILE_BLOCK,
    (2, 5): TILE_BLOCK, (3, 5): TILE_BLOCK,
    (0, 6): TILE_BLOCK, (1, 6): TILE_BLOCK,
    (2, 6): TILE_BLOCK, (3, 6): TILE_BLOCK
}

# Game
class Game:
    def __init__(self):
        """ Constructor """

        # Pyxel
        pyxel.init(W, H, title="Hello, Pyxel!!", fps=50)
        pyxel.load("my_resource.pyxres")

        # Tilemap(Copy 0 -> 1)
        pyxel.tilemaps[1].blt(0, 0, 0, 0, 0, 640, 128)

        # Score
        self.score = 0
        # Counter
        self.counter = self.count_coins()

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

        # Player x Coins
        u, v = self.get_uv(self.player.x, self.player.y)
        tile = self.get_tile(u, v)
        if tile in TILE_COINS:
            self.score += 1 # Score
            self.counter -= 1 # Counter
            self.set_tile(u, v, (0, 0)) # Delete
            if 0 < self.counter:
                pyxel.play(1, 4, loop=False) # サウンド
            else:
                pyxel.play(1, 6, loop=False) # サウンド

    def draw(self):
        pyxel.cls(0)

        # Camera(on)
        self.camera_on()

        # Tilemap
        pyxel.bltm(0, 0, 0, 0, 0, 640, 128, 0)

        # Player
        self.player.draw()

        # Camera(off)
        self.camera_off()

        # Score
        pyxel.text(1, 1, 
            "SCORE:{:04}".format(self.score), 7)
        pyxel.text(92, 1, 
            "REST:{:04}".format(self.counter), 7)

        # CLEAR
        if self.counter <= 0:
            pyxel.text(42, H-8, "GAME CLEAR!!", 7)

    def controll(self):

        # Player
        from_u, from_v = self.get_uv(self.player.x, self.player.y)
        if pyxel.btnp(pyxel.KEY_W):
            to_u, to_v = self.search_block(from_u, from_v, 0, -1)
            self.player.go(4, to_u, to_v)
            pyxel.play(0, 0, loop=False) # サウンド
            return
        if pyxel.btnp(pyxel.KEY_A):
            to_u, to_v = self.search_block(from_u, from_v, -1, 0)
            self.player.go(4, to_u, to_v)
            pyxel.play(0, 0, loop=False) # サウンド
            return
        if pyxel.btnp(pyxel.KEY_S):
            to_u, to_v = self.search_block(from_u, from_v, 0, 1)
            self.player.go(4, to_u, to_v)
            pyxel.play(0, 0, loop=False) # サウンド
            return
        if pyxel.btnr(pyxel.KEY_D):
            to_u, to_v = self.search_block(from_u, from_v, 1, 0)
            self.player.go(4, to_u, to_v)
            pyxel.play(0, 0, loop=False) # サウンド
            return

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

    def get_uv(self, x, y):
        return (x//8, y//8)

    def get_tile(self, u, v):
        return pyxel.tilemaps[0].pget(u, v)

    def set_tile(self, u, v, tile):
        pyxel.tilemaps[0].pset(u, v, tile)

    def search_block(self, from_u, from_v, off_u, off_v):
        to_u = from_u + off_u
        to_v = from_v + off_v
        if to_u < 0: return from_u, from_v
        if to_v < 0: return from_u, from_v
        if 15 < to_u: return from_u, from_v
        if 15 < to_v: return from_u, from_v 
        tile = self.get_tile(to_u, to_v)
        if tile in TILE_BLOCKS:
            return from_u, from_v
        return self.search_block(to_u, to_v, off_u, off_v)

    def count_coins(self):
        tilemap = pyxel.tilemaps[0]
        w = tilemap.width
        h = tilemap.height
        counter = 0
        for u in range(w):
            for v in range(h):
                tile = tilemap.pget(u, v)
                if tile in TILE_COINS:
                    counter += 1
        return counter

def main():
    """ Main """
    Game()

if __name__ == "__main__":
    main()