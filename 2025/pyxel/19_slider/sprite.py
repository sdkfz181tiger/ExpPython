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
        self.vx = 0
        self.vy = 0

    def update(self):
        dx = self.to_x - self.x
        dy = self.to_y - self.y

        if abs(dx) < 4:
            self.x = self.to_x
            self.vx = 0
        else:
            #self.x += dx / 4
            self.x += self.vx

        if abs(dy) < 4:
            self.y = self.to_y
            self.vy = 0
        else:
            #self.y += dy / 4
            self.y += self.vy

    def draw(self):
        pyxel.blt(self.x, self.y, 0, 
            self.u, self.v,
            self.w, self.h, 0)

    def go(self, spd, to_u, to_v):
        if self.is_moving(): return
        self.to_x = to_u * 8
        self.to_y = to_v * 8
        dx = self.to_x - self.x
        dy = self.to_y - self.y
        rad = math.atan2(dy, dx)
        self.vx = math.cos(rad) * spd
        self.vy = math.sin(rad) * spd

    def is_moving(self):
        if self.x != self.to_x: return True
        if self.y != self.to_y: return True
        return False

class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ Constructor """
        super().__init__(x, y, u, v)

    def update(self):
        super().update()

    def draw(self):
        super().draw()
        if not self.is_moving(): return
        dx = self.to_x - self.x
        dy = self.to_y - self.y

        # Left or Right
        if dx == 0:
            pass
        elif 0 < dx:
            pyxel.blt(self.x-8, self.y, 0, 
                self.u+16, self.v,
                self.w, self.h, 0)
        else:
            pyxel.blt(self.x+8, self.y, 0, 
                self.u+24, self.v,
                self.w, self.h, 0)

        # Up or Down
        if dy == 0:
            pass
        elif 0 < dy:
            pyxel.blt(self.x, self.y-8, 0, 
                self.u+16, self.v+8,
                self.w, self.h, 0)
        else:
            pyxel.blt(self.x, self.y+8, 0, 
                self.u+24, self.v+8,
                self.w, self.h, 0)
