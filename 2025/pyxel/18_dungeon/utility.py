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
        max_x, max_y):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.img = img
        self.u = u
        self.v = v
        self.w = w
        self.h = h
        self.max_x = max_x
        self.max_y = max_y
        
    def update(self):
        """ 更新処理 """
        pass

    def draw(self):
        """ 描画処理 """
        
        pyxel.bltm(self.x, self.y, self.img,
            self.u, self.v, self.w, self.h)
        

    