# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math

class BaseSprite(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y
        # Velocity
        self.vx = 0
        self.vy = 0
        # Animation
        self.anim_counter = 0 # カウンタ
        self.anim_interval = 4 # 4フレームおきにカウント
        self.anim_index = 0 # フレーム番号
        self.anim = [] # テクスチャを格納するリスト

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx * delta_time
        self.center_y += self.vy * delta_time
        # Animation
        self.update_animation()

    def move(self, spd, deg):
        """ Move Sprite """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def stop(self):
        """ Stop Sprite """
        self.vx = 0
        self.vy = 0

    def update_animation(self):
        """ Animation """
        if not self.anim: return
        self.anim_counter += 1 # カウンタに+1
        if(self.anim_counter < self.anim_interval): return # 4フレームおきにカウント
        self.anim_counter = 0 # カウンタをリセット
        self.anim_index += 1 # テクスチャ番号を次へ
        if len(self.anim) <= self.anim_index: self.anim_index = 0 # 最後であれば0に
        self.texture = self.anim[self.anim_index] # テクスチャをセット

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # アニメーション用のテクスチャを5枚読み込む
        self.anim.append(arcade.load_texture("images/ninja/front_01.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_02.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_03.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_04.png"))
        self.anim.append(arcade.load_texture("images/ninja/front_05.png"))

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
