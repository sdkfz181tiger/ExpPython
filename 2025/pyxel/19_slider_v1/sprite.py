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
TILE_COINS = {
    (0, 4): TILE_COIN
}

# u, v
TILE_BLOCKS = {
    (0, 4): TILE_BLOCK
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
        self.next_x = x
        self.next_y = y

    def update(self):
        dx = self.next_x - self.x
        dy = self.next_y - self.y
        if abs(dx) < 4: 
            self.x = self.next_x
        else:
            self.x += dx / 2
        if abs(dy) < 4: 
            self.y = self.next_y
        else:
            self.y += dy / 2

    def draw(self):
        pass

class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v)

    def update(self):
        super().update()

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 
            self.u, self.v,
            self.w, self.h, 0)

    def go(self, off_u, off_v):
        if self.is_moving(): return
        from_u, from_v = self.get_uv(self.x, self.y)
        next_u, next_v = self.search_block(from_u, from_v, off_u, off_v)
        self.next_x = next_u * 8
        self.next_y = next_v * 8

    def search_block(self, from_u, from_v, off_u, off_v):
        next_u = from_u + off_u
        next_v = from_v + off_v
        if next_u < 0: return from_u, from_v
        if next_v < 0: return from_u, from_v
        if 15 < next_u: return from_u, from_v
        if 15 < next_v: return from_u, from_v 
        tile = self.get_tile(next_u, next_v)
        if tile in TILE_BLOCKS:
            return from_u, from_v
        return self.search_block(next_u, next_v, off_u, off_v)

    def is_moving(self):
        if self.x != self.next_x: return True
        if self.y != self.next_y: return True
        return False

    def get_uv(self, x, y):
        return (x//8, y//8)

    def get_tile(self, u, v):
        return pyxel.tilemaps[0].pget(u, v)
