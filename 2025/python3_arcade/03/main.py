# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random
import sprite

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

        # FPS, Elapsed
        self.elapsed = 0.0
        self.fps = 0.0

    def reset(self):
        pass

    def on_update(self, delta_time):
        self.elapsed += delta_time
        self.fps = 1.0 / delta_time

    def on_draw(self):
        self.clear() # 背景色でクリア

        # Elapsed
        msg = "Elapsed: {:.2f}".format(self.elapsed)
        arcade.draw_text(msg, 20, 20,
                         arcade.color.WHITE,
                         FONT_SIZE, anchor_x="left")

        # FPS
        msg = "FPS: {:.2f}".format(self.fps)
        arcade.draw_text(msg, W-20, 20,
                         arcade.color.WHITE,
                         FONT_SIZE, anchor_x="right")

    def on_key_press(self, key, key_modifiers):
        pass

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