# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import src.sprite as sprite
import src.utility as utility
import src.game as game

# Title
class TitleView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background_color = arcade.color.PRUNE

        # Info
        self.msg_info = arcade.Text(
            "TITLE: SPACE TO NEXT", 
            window.width/2, window.height-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Game
        if key == arcade.key.SPACE:
            view = game.GameView(self.window) # GameView
            self.window.show_view(view)

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()