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

    def __init__(self, filename, scale):
        super().__init__(filename, scale=scale)
        self.vx = 0
        self.vy = 0

    def set_position(self, x, y):
        self.center_x = x
        self.center_y = y

    def update(self, delta_time):
        self.center_x += self.vx
        self.center_y += self.vy
