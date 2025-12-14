# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random

# ステータス
class Stats:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.key = ""
        self.elapsed = 0.0
        self.fps = 0.0
        self.font_color = arcade.color.WHITE
        self.font_size = 12

    def key_press(self, key):
        self.key = key

    def update(self, delta_time):
        # Delta
        self.elapsed += delta_time
        # FPS
        self.fps = 1.0 / delta_time

    def draw(self):

        # Key
        msg = "Key: {}".format(self.key)
        arcade.draw_text(msg, 20, 20,
                         self.font_color, self.font_size, 
                         anchor_x="left")

        # Elapsed
        msg = "Elapsed: {:.2f}".format(self.elapsed)
        arcade.draw_text(msg, self.w/2, 20,
                         self.font_color, self.font_size, 
                         anchor_x="center")

        # FPS
        msg = "FPS: {:.2f}".format(self.fps)
        arcade.draw_text(msg, self.w-20, 20,
                         self.font_color, self.font_size, 
                         anchor_x="right")



