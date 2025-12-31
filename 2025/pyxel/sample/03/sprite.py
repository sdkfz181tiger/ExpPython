# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel as px
import math
import random

class BaseSprite:

    def __init__(self, x, y, w=8, h=8):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0

    def update(self):
        """ 更新処理 """
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """ 描画処理 """
        pass

    def move(self, spd, deg):
        """ 移動 """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def stop(self):
        """ 停止 """
        self.vx = 0
        self.vy = 0

    def flip_x(self):
        """ x方向反転 """
        self.vx *= -1

class ShipSprite(BaseSprite):

    def __init__(self, x, y):
        super().__init__(x, y)

    def draw(self):
        """ 描画処理 """
        off_y = px.frame_count % 3
        px.blt(self.x, self.y, 0, 0, 0, 
                self.w, self.h, 0) # Ship
        px.blt(self.x, self.y+self.h, 0, 0, self.h+off_y, 
                self.w, self.h, 0) # Fire

class BulletSprite(BaseSprite):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.x += self.w / 2 - 1 # Offset

    def draw(self):
        """ 描画処理 """
        px.rect(self.x, self.y, 2, 2, 12)
