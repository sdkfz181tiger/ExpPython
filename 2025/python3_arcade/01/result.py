# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import sprite
import random

import title

# Result
class ResultView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background_color = arcade.color.PAYNE_GREY

        # Message
        self.msg_info = arcade.Text(
            "SPACE TO TITLE", 
            window.width/2, window.height-20,
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Game
        if key == arcade.key.SPACE: 
            self.window.show_view(title.TitleView(self.window)) # TitleView

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()