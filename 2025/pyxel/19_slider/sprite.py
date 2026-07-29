# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

TILE_NONE  = 0
TILE_COIN  = 1
TILE_BLOCK = 2

# u, v
TILE_TYPES = {
    (0, 2): TILE_COIN, # Coin
    (0, 4): TILE_BLOCK # Block
}

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ Constructor """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h

    def update(self):
        pass

    def draw(self):
        pass

    def intersects(self, other):
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

    def go_left(self):
        x = self.x - 8
        y = self.y
        tilemap = pyxel.tilemaps[0]
        flg, u, v = self.is_tile_type(x, y, TILE_BLOCK)
        if flg: return
        flg, u, v = self.is_tile_type(x, y, TILE_COIN)
        if flg:
            tilemap.pset(u, v, (0, 0)) # Get
        self.x = u * 8
        self.y = v * 8

    def go_right(self):
        x = self.x + 8
        y = self.y
        tilemap = pyxel.tilemaps[0]
        flg, u, v = self.is_tile_type(x, y, TILE_BLOCK)
        if flg: return
        flg, u, v = self.is_tile_type(x, y, TILE_COIN)
        if flg:
            tilemap.pset(u, v, (0, 0)) # Get
        self.x = u * 8
        self.y = v * 8

    def go_up(self):
        x = self.x
        y = self.y - 8
        tilemap = pyxel.tilemaps[0]
        flg, u, v = self.is_tile_type(x, y, TILE_BLOCK)
        if flg: return
        flg, u, v = self.is_tile_type(x, y, TILE_COIN)
        if flg:
            tilemap.pset(u, v, (0, 0)) # Get
        self.x = u * 8
        self.y = v * 8

    def go_down(self):
        x = self.x
        y = self.y + 8
        tilemap = pyxel.tilemaps[0]
        flg, u, v = self.is_tile_type(x, y, TILE_BLOCK)
        if flg: return
        flg, u, v = self.is_tile_type(x, y, TILE_COIN)
        if flg:
            tilemap.pset(u, v, (0, 0)) # Get
        self.x = u * 8
        self.y = v * 8

    def is_tile_type(self, x, y, type):
        tilemap = pyxel.tilemaps[0]
        u, v = x // 8, y // 8
        tile = tilemap.pget(u, v)
        if not(tile in TILE_TYPES):
            return False, u, v
        return TILE_TYPES[tile] == type, u, v

class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v)
        self.off_u = 0
        self.off_v = 0

    def update(self):
        super().update()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 
            self.u + self.off_u, 
            self.v + self.off_v, 
            self.w, self.h, 0)
