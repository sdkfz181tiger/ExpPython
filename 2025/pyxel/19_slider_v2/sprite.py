# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ Constructor """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.to_x = x
        self.to_y = y

    def update(self):
        dx = self.to_x - self.x
        dy = self.to_y - self.y
        if abs(dx) < 4: 
            self.x = self.to_x
        else:
            self.x += dx / 2
        if abs(dy) < 4: 
            self.y = self.to_y
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

    def go(self, to_u, to_v):
        if self.is_moving(): return
        self.to_x = to_u * 8
        self.to_y = to_v * 8

    def is_moving(self):
        if self.x != self.to_x: return True
        if self.y != self.to_y: return True
        return False
