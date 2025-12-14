# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random
import sprite
import utility

# キャンバスの幅と高さ
W, H = 480, 320

# タイトル
TITLE = "Hello, Arcade!!"

# Font
FONT_SIZE = 10

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.AMAZON
        self.utility = utility.Utility(W, H) # Utility

    def reset(self):
        pass

    def on_key_press(self, key, key_modifiers):
        self.utility.key_press(key) # Utility

    def on_update(self, delta_time):
        self.utility.update(delta_time) # Utility

    def on_draw(self):
        self.clear() # 背景色でクリア
        self.utility.draw_stats() # Utility

def main():
    """ メイン処理 """

    # Window
    window = arcade.Window(W, H, TITLE)

    # GameView
    game = GameView()

    # Show
    window.show_view(game)

    # Run
    arcade.run()

if __name__ == "__main__":
    main()