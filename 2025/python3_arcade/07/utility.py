# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random

# ユーティリティクラス
class Utility:

    def __init__(self, w, h):
        self.w = w
        self.h = h
        self.key = "*"
        self.elapsed = 0.0
        self.fps = 0.0
        self.font_color = arcade.color.WHITE
        self.font_size = 12
        self.text_objects = []

        # Key
        self.text_key = arcade.Text(
            "", 20, 20, arcade.color.WHITE,
            self.font_size, anchor_x="left")
        self.text_objects.append(self.text_key)

        # Elapsed
        self.text_elapsed = arcade.Text(
            "", w/2, 20, arcade.color.WHITE,
            self.font_size, anchor_x="center")
        self.text_objects.append(self.text_elapsed)

        # FPS
        self.text_fps = arcade.Text(
            "", w-20, 20, arcade.color.WHITE,
            self.font_size, anchor_x="right")
        self.text_objects.append(self.text_fps)

    def key_press(self, key):
        self.key = key

    def update(self, delta_time):
        # Delta
        self.elapsed += delta_time
        # FPS
        self.fps = 1.0 / delta_time

    def draw_stats(self):

        # Key
        self.text_key.text = "Key: {}".format(self.key)

        # Elapsed
        self.text_elapsed.text = "Elapsed: {:.2f}".format(self.elapsed)

        # FPS
        self.text_fps.text = "FPS: {:.2f}".format(self.fps)

        # Draw
        for text_object in self.text_objects: text_object.draw()




