# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random

class Shape:

    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.vx = 0
        self.vy = 0
        self.dead = False

    def update(self, delta_time):
        # Update
        self.x += self.vx * delta_time
        self.y += self.vy * delta_time

    def draw(self):
        # Draw
        arcade.draw_ellipse_filled(self.x, self.y,
                                   self.r, self.r,
                                   arcade.color.WHITE, 0.0)

class Ninja(arcade.Sprite):

    def __init__(self, filename, x, y, scale):
        super().__init__(filename, scale=scale)
        self.center_x = x
        self.center_y = y
        self.vx = 0
        self.vy = 0

        # Animation
        self.anim_interval = 4
        self.anim_counter = 0
        self.anim_index = 0
        self.anim_key = ""
        self.anims = {}

    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx * delta_time
        self.center_y += self.vy * delta_time
        self.update_animation() # Animation

    def update_animation(self):
        """ Animation """
        if not self.anim_key in self.anims: return
        self.anim_counter += 1
        if(self.anim_interval < self.anim_counter):
            self.anim_counter = 0
            self.anim_index += 1
            anim = self.anims[self.anim_key]
            if len(anim) <= self.anim_index: self.anim_index = 0
            self.texture = anim[self.anim_index]

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
