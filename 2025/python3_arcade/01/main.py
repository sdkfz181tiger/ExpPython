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

# フレームレート
F_RATE = 30 # 1秒間に実行するフレーム回数
F_INTERVAL = int(1000 / F_RATE) # 1フレームの間隔

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.AMAZON

    def reset(self):
        pass

    def on_draw(self):
        self.clear() # 背景色でクリア

    def on_update(self, delta_time):
        pass

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