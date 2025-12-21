# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import src.sprite as sprite
import src.utility as utility
import src.title as title

# Result
class ResultView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background_color = arcade.color.CERULEAN

        # Info
        self.msg_info = arcade.Text(
            "RESULT: SPACE TO NEXT", 
            window.width/2, window.height-20,
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Title
        if key == arcade.key.SPACE:
            view = title.TitleView(self.window) # TitleView
            self.window.show_view(view)

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()