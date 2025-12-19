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

    def update(self, delta_time):
        """ Update """
        self.center_x += self.vx * delta_time
        self.center_y += self.vy * delta_time

    def move(self, spd, deg):
        """ Move Sprite """
        rad = deg * math.pi / 180
        self.vx = spd * math.cos(rad)
        self.vy = spd * math.sin(rad)

    def stop(self):
        """ Stop Sprite """
        self.vx = 0
        self.vy = 0

class Player(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

class Coin(BaseSprite):

    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)
