# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

class MapManager:

    def __init__(self, 
        x, y, img, u, v, w, h,
        map_w, map_h):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.img = img
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.map_w = map_w
        self.map_h = map_h
        
    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        pyxel.bltm(self.x, self.y, self.img,
            self.u, self.v, self.w, self.h)

    def getXY(self, r, c):
        x = c * 8 - self.u
        y = r * 8 - self.v
        return (x, y)

    def offUV(self, u, v):
        """ 表示座標オフセット """
        self.u += u
        self.v += v
        self.adjustUV()

    def setUV(u, v):
        """ 表示座標指定 """
        self.u = u
        self.v = v
        self.adjustUV()

    def adjustUV(self):
        if self.u < 0:
            self.u = 0
        if self.map_w < (self.u + self.w):
            self.u = self.map_w - self.w
        if self.v < 0:
            self.v = 0
        if self.map_h < (self.v + self.h):
            self.v = self.map_h - self.h
