# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math # 数学的計算をするモジュール

class BaseSprite(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y
        # Velocity
        self.vx = 0 # x方向の速度
        self.vy = 0 # y方向の速度

    def update(self, delta_time):
        """ Update """
        super().update(delta_time)
        self.center_x += self.vx * delta_time # x座標を更新
        self.center_y += self.vy * delta_time # y座標を更新

    def move(self, spd, deg):
        """ Move Sprite """
        rad = deg * math.pi / 180 # 度数法から弧度法へ変換
        self.vx = spd * math.cos(rad) # x方向の速度
        self.vy = spd * math.sin(rad) # y方向の速度

    def stop(self):
        """ Stop Sprite """
        self.vx = 0 # x方向の速度を0に
        self.vy = 0 # y方向の速度を0に

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
