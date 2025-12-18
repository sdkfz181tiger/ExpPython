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
        super().__init__()

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # 背景リストを用意する
        self.backgrounds = arcade.SpriteList()

        # 背景スプライトを作る
        bkg = arcade.Sprite("images/bg_temple.png")
        bkg.center_x = W/2
        bkg.center_y = H/2

        self.backgrounds.append(bkg)# 背景リストに追加する

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):
        pass

    def on_draw(self):
        self.clear() # Clear
        self.backgrounds.draw() # 背景リストを描画

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