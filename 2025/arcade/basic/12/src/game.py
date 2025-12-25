# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import src.sprite as sprite
import src.utility as utility
import src.result as result

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.background_color = arcade.color.DARK_SPRING_GREEN

        # Info
        self.msg_info = arcade.Text(
            "GAME: SPACE TO NEXT", 
            window.width/2, window.height-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        # Space to Result
        if key == arcade.key.SPACE: 
            view = result.ResultView(self.window) # ResultView
            self.window.show_view(view)

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()