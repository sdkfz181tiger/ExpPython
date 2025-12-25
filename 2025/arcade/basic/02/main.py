# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random

class GameView(arcade.View):

    def __init__(self, window):
        super().__init__()
        self.window = window
        self.w = self.window.width # ゲーム画面の幅
        self.h = self.window.height # ゲーム画面の高さ

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
    window = arcade.Window(480, 320, "Hello, Arcade!!")
    game = GameView(window)
    window.show_view(game)
    arcade.run()

if __name__ == "__main__":
    main()