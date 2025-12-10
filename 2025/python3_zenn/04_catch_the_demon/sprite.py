# coding: utf-8

"""
かじるプログラミング_tkinter
"""

import math
import random
import tkinter

# 鬼クラス
class DemonSprite:

    def __init__(self, cvs, x, y, r):
        self.x = x # x座標
        self.y = y # y座標
        self.r = r # 円の半径
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="white", width=0)

    def update(self, cvs):
        
        # 円の座標を更新
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)
