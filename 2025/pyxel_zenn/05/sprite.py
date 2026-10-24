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
        self.x = x # x座標
        self.y = y # y座標
        self.w = w # 画像の幅
        self.h = h # 画像の高さ
        self.vx = 0 # 移動速度(x方向)
        self.vy = 0 # 移動速度(y方向)

    def update(self):
        """ 更新処理 """
        self.x += self.vx # x方向に移動
        self.y += self.vy # y方向に移動

    def draw(self):
        """ 描画処理(派生クラスで実装) """
        pass

class ShipSprite(BaseSprite):

    def __init__(self, x, y):
        """ コンストラクタ """
        super().__init__(x, y)

    def draw(self):
        """ 描画処理 """
        pyxel.blt(self.x, self.y, 0, 
            0, 0, 
            self.w, self.h, 0) # Ship