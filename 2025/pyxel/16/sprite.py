# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

class BaseSprite:

    def __init__(self, x, y, u, v, w=8, h=8):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.vx = 0
        self.vy = 0
        self.right_flg = True # 右向きフラグ

    def update(self):
        """ 更新処理 """
        self.x += self.vx
        self.y += self.vy

    def draw(self):
        """ 描画処理 """
        u = 0 if self.right_flg else 8
        pyxel.blt(self.x, self.y, 0, 
            self.u + u, self.v, self.w, self.h, 0)

    def move(self, spd, deg):
        """ 移動 """
        rad = (deg * math.pi) / 180
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度

    def stop(self):
        """ 停止 """
        self.move(0, 0) # 停止

    def intersects(self, other):
        """ 矩形同士の当たり判定(AABB) """
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v):
        """ コンストラクタ """
        super().__init__(x, y, u, v)

    def update(self):
        """ 更新処理 """
        super().update()

    def go_up(self, spd):
        self.move(spd, 270)

    def go_left(self, spd):
        self.move(spd, 180)
        self.right_flg = False # 右向きフラグ

    def go_down(self, spd):
        self.move(spd, 90)

    def go_right(self, spd):
        self.move(spd, 0)
        self.right_flg = True # 右向きフラグ
