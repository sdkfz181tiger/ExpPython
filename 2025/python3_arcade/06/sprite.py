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
        self.anim = self.load_animation("images/ninja_{:02d}.png", 5)

    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y
        self.update_animation() # Animation

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx
        self.center_y += self.vy

    def update_animation(self):
        """ Animation """
        self.anim_counter += 1
        if(self.anim_interval < self.anim_counter):
            self.anim_counter = 0
            self.anim_index += 1
            if len(self.anim) <= self.anim_index: self.anim_index = 0
            self.texture = self.anim[self.anim_index]

    def load_animation(self, filename, num):
        """ Load Texture """
        textures = []
        for i in range(num):
            path = filename.format(i+1)
            textures.append(arcade.load_texture(path))
        return textures
