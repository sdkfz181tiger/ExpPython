# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random

W, H = 480, 320 # ゲーム画面の幅と高さ
TITLE = "Hello, Arcade!!" # タイトル

class GameView(arcade.View):

    def __init__(self):
        """ 初期化 """
        super().__init__()
        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

    def on_key_press(self, key, key_modifiers):
        """ キーを押した時 """
        pass

    def on_key_release(self, key, key_modifiers):
        """ キーを離した時 """
        pass

    def on_update(self, delta_time):
        """ 更新処理 """
        pass

    def on_draw(self):
        """ 描画処理 """
        self.clear() # Clear

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