# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random

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
        self.anim_interval = 4
        self.anim_counter = 0
        self.anim_index = 0
        self.anim_key = ""
        self.anim_pause = False
        self.anims = {}

    def update(self, delta_time):
        """ Update """
        super().update(delta_time)
        self.center_x += self.vx * delta_time
        self.center_y += self.vy * delta_time
        self.update_animation() # Animation

    def set_x(self, x):
        self.center_x = x

    def set_y(self, y):
        self.center_y = y

    def move(self, spd, deg, tag=""):
        """ Move Sprite """
        rad = deg * math.pi / 180 # Radian
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)
        if 0 < len(tag): self.change_animation(tag) # Animation

    def stop(self):
        """ Stop Sprite """
        self.vx = 0
        self.vy = 0
        self.stop_animation() # Animation

    def load_animation(self, key, filename, num):
        """ Load Animation """
        anim = []
        for i in range(num):
            path = filename.format(i+1)
            anim.append(arcade.load_texture(path))
        self.anims[key] = anim

    def change_animation(self, key):
        """ Change Animation """
        if not key in self.anims: return
        self.anim_counter = 0
        self.anim_index = 0
        self.anim_key = key
        self.texture = self.anims[key][0]
        self.start_animation()

    def start_animation(self):
        """ Start Animation """
        self.anim_pause = False

    def stop_animation(self):
        """ Stop Animation """
        self.anim_pause = True

    def update_animation(self):
        """ Update Animation """
        if not self.anim_key in self.anims: return
        if self.anim_pause: return
        self.anim_counter += 1
        if(self.anim_interval < self.anim_counter):
            self.anim_counter = 0
            self.anim_index += 1
            anim = self.anims[self.anim_key]
            if len(anim) <= self.anim_index: self.anim_index = 0
            self.texture = anim[self.anim_index]

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # Animation
        self.load_animation("front", "images/ninja/front_{:02d}.png", 5)
        self.load_animation("left", "images/ninja/left_{:02d}.png", 5)
        self.load_animation("right", "images/ninja/right_{:02d}.png", 5)
        self.load_animation("back", "images/ninja/back_{:02d}.png", 5)

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        # Animation
        self.load_animation("coin", "images/koban/koban_{:02d}.png", 5)
        self.change_animation("coin")
