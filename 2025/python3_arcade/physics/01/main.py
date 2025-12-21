# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import random
import sprite

# Game
class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width
        self.h = self.window.height

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # Info
        self.msg_info = arcade.Text(
            "GAME", 
            self.w/2, self.h-20, 
            arcade.color.WHITE, 12,
            anchor_x="center", anchor_y="top")

    def on_key_press(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.msg_info.draw()

def main():
    """ メイン処理 """
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    window.show_view(GameView(window)) # GameView
    arcade.run()

if __name__ == "__main__":
    main()