# coding: utf-8

"""
かじるプログラミング_arcade
"""

import math
import random

# 鬼クラス
class DemonSprite:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.dead = False

    def update(self):
        pass

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

    def die(self):
        self.dead = True
        self.stop()

    def is_dead(self):
        return self.dead

    def is_inside(self, x, y):
        dist_x = (self.x - x) ** 2
        dist_y = (self.y - y) ** 2
        dist = (dist_x + dist_y) ** 0.5
        return dist < self.r
