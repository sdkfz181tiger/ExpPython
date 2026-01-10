# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

class BaseSprite:

    def __init__(self, x, y, u, v, spd, w=8, h=8):
        """ コンストラクタ """
        self.x = x
        self.y = y
        self.u = u
        self.v = v
        self.spd = spd
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

    def get_center(self):
        """ 中心座標 """
        return (self.x + self.w/2, self.y + self.h/2)

    def set_center(self, x, y):
        """ 中心座標 """
        self.x = x - self.w / 2
        self.y = y - self.h / 2

    def move(self, deg):
        """ 移動 """
        rad = (deg * math.pi) / 180
        self.vx = self.spd * math.cos(rad) # x方向の速度
        self.vy = self.spd * math.sin(rad) # y方向の速度
        if deg == 90 or deg == 270: return
        self.right_flg = not (90 < deg and deg < 270) # 右向きフラグ

    def stop(self):
        """ 停止 """
        self.vx = 0
        self.vy = 0

    def intersects(self, other):
        """ 矩形同士の当たり判定(AABB) """
        if other.x + other.w < self.x: return False
        if self.x + self.w < other.x: return False
        if other.y + other.h < self.y: return False
        if self.y + self.h < other.y: return False
        return True

    def get_distance(self, other):
        """ 距離を計算する """
        d_x = self.x - other.x
        d_y = self.y - other.y
        return math.sqrt(d_x*d_x + d_y*d_y)

    def get_direction(self, other):
        """ 方向を計算する """
        d_x = other.x - self.x
        d_y = other.y - self.y
        rad = math.atan2(d_y, d_x)
        return (rad * (180 / math.pi) + 360) % 360

class PlayerSprite(BaseSprite):

    def __init__(self, x, y, u, v, spd, game):
        """ コンストラクタ """
        super().__init__(x, y, u, v, spd)
        self.shot_interval = 8
        self.shot_counter = 0
        self.game = game

    def update(self):
        """ 更新処理 """
        super().update()
        # Shot
        self.shot_counter += 1
        if self.shot_interval < self.shot_counter:
            self.shot_counter = 0
            self.game.on_shot_event(self) # Shot

class Monster(BaseSprite):

    def __init__(self, x, y, u, v, spd, think_interval, target):
        """ コンストラクタ """
        super().__init__(x, y, u, v, spd)
        self.think_interval = think_interval
        self.think_counter = 0
        self.target = target

    def update(self):
        """ 更新処理 """
        super().update()
        # Think
        self.think_counter += 1
        if self.think_interval < self.think_counter:
            self.think_counter = 0
            direction = self.get_direction(self.target)
            self.move(direction)

class Bullet(BaseSprite):

    def __init__(self, x, y, spd, life=10):
        """ コンストラクタ """
        super().__init__(x, y, 0, 0, spd)
        self.life = life

    def update(self):
        """ 更新処理 """
        super().update()
        self.life -= 1
        if self.life < 0: 
            self.stop()

    def draw(self):
        """ 描画処理 """
        pyxel.rect(self.x, self.y, 2, 2, 12)

    def is_dead(self):
        """ 死亡フラグ """
        return self.life < 0
