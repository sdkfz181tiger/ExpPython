# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

class BaseSprite:

    def __init__(self, x, y, w=8, h=8):
        """ コンストラクタ """
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
        """ 描画処理(派生クラスで実装) """
        pass

    def move(self, spd, deg):
        """ 移動 """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

class ShipSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)
        self.index = random.randint(0, 1) # プレイヤー画像

    def draw(self):
        """ 描画処理 """
        off_y = pyxel.frame_count % 3 # 炎をパタパタさせる
        pyxel.blt(self.x, self.y, 0, 
            self.w*self.index, 0, 
            self.w, self.h, 0) # Ship
        pyxel.blt(self.x, self.y+self.h, 0, 
            self.w*self.index, self.h+off_y, 
            self.w, self.h, 0) # Fire
