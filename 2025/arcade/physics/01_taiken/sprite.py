# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import math

class BaseSprite(arcade.Sprite):

    def __init__(self, filename, x, y):
        super().__init__(filename)
        # Position
        self.center_x = x
        self.center_y = y
        # Animation
        self.anim_dict = {}
        self.anim_interval = 6
        self.anim_counter = 0
        self.anim_index = 0 # フレーム番号
        self.anim_key = "" # 再生中のアニメ

    def add_animation(self, key, arr):
        self.anim_dict[key] = []
        for path in arr:
            self.anim_dict[key].append(arcade.load_texture(path))

    def change_animation(self, key):
        if not key in self.anim_dict: return
        self.anim_index = 0 # フレーム番号
        self.anim_key = key # 再生中のアニメ

    def update_animation(self):
        if not self.anim_key in self.anim_dict: return
        anim = self.anim_dict[self.anim_key]
        self.anim_counter += 1 # Counter
        if(self.anim_counter < self.anim_interval): return
        self.anim_counter = 0
        self.anim_index += 1 # Index
        if len(anim) <= self.anim_index: self.anim_index = 0
        self.texture = anim[self.anim_index]


class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
        # Animation
        self.add_animation("stand", [
            "images/ninja/stand_01.png", "images/ninja/stand_02.png",
            "images/ninja/stand_03.png", "images/ninja/stand_04.png",
            "images/ninja/stand_05.png"])
        self.add_animation("jump", [
            "images/ninja/front_01.png", "images/ninja/front_02.png",
            "images/ninja/front_03.png", "images/ninja/front_04.png",
            "images/ninja/front_05.png"])

        self.change_animation("stand")


class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
        # Animation
        self.add_animation("stand", [
            "images/coin/coin_01.png", "images/coin/coin_02.png",
            "images/coin/coin_03.png", "images/coin/coin_04.png",
            "images/coin/coin_05.png"])
        self.change_animation("stand")

class Block(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
