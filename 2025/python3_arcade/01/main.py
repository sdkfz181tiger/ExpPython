# coding: utf-8

"""
かじるプログラミング_arcade
"""

import arcade
import math
import random
import sprite
import utility

W, H = 480, 320 # ゲーム画面の幅と高さ
TITLE = "Hello, Arcade!!" # タイトル
FONT_SIZE = 10 # フォントサイズ
SPRITE_SCALE = 1 # スプライトの倍率
PLAYER_SPEED = 90 # プレイヤーの速度

class GameView(arcade.View):

    def __init__(self):
        super().__init__()

        # 背景色
        self.background_color = arcade.color.PAYNE_GREY

        # Player
        self.players = arcade.SpriteList()
        self.player = sprite.Player("images/ninja/front_01.png",
                                    x=W/2, y=H/2)
        self.players.append(self.player)

    def on_key_press(self, key, key_modifiers):
        pass

    def on_key_release(self, key, key_modifiers):
        pass

    def on_update(self, delta_time):

        # Update
        self.players.update()

    def on_draw(self):
        self.clear() # Clear
        self.players.draw() # Draw

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