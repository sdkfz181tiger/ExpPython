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
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.dead = False # 死亡フラグ
        # 円
        self.oval = cvs.create_oval(x-r, y-r, x+r, y+r,
                                    fill="white", width=0)

    def update(self, cvs):

        self.x = self.x + self.vx
        self.y = self.y + self.vy
        
        cvs.coords(self.oval,
                   self.x - self.r, self.y - self.r,
                   self.x + self.r, self.y + self.r)

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def move(self, spd, deg):
        radian = deg * math.pi / 180
        self.vx = spd * math.cos(radian)
        self.vy = spd * math.sin(radian)

    def stop(self):
        self.move(0, 0)

    def die(self, cvs):
        self.dead = True # 死亡フラグをTrueに
        self.stop() # 停止する
        # 円の色を更新
        cvs.itemconfig(self.oval, fill="red")

    def is_dead(self):
        return self.dead # 死亡フラグを返す

    def is_hit(self, x, y):
        dist_x = (self.x - x) ** 2 # スプライトの水平方向の距離
        dist_y = (self.y - y) ** 2 # スプライトの垂直方向の距離
        dist = (dist_x + dist_y) ** 0.5 # スプライトとの距離
        return dist < self.r # スプライトとの距離が半径以内ならヒット(True)
