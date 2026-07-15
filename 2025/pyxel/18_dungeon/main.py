# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite
import utility

W, H = 160, 120

START_X = W / 2
START_Y = H / 2
PLAYER_SPD = 1

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        # マップを初期化
        self.map = utility.MapManager(0, 0, 0, 0, 0, W, H, 256, 256)

        # プレイヤーを初期化
        self.player = sprite.PlayerSprite(
            START_X, START_Y, 0, 72, PLAYER_SPD, self)

        pyxel.run(self.update, self.draw) # Pyxel実行

    def update(self):
        """ 更新処理 """

        # コントロール
        self.control()

        # プレイヤーを更新
        self.player.update()

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # タイルマップを描画
        self.map.draw()

        # プレイヤーを描画
        self.player.draw()

    def control(self):

        # タイルマップスクロール
        # if pyxel.btn(pyxel.KEY_A):
        #     self.scroll_u += 1
        # if pyxel.btn(pyxel.KEY_D):
        #     self.scroll_u -= 1

        # W
        if pyxel.btnp(pyxel.KEY_W):
            self.player.move(270)
        elif pyxel.btnr(pyxel.KEY_W):
            self.player.stop()
        # A
        if pyxel.btnp(pyxel.KEY_A):
            self.player.move(180)
        elif pyxel.btnr(pyxel.KEY_A):
            self.player.stop()
        # S
        if pyxel.btnp(pyxel.KEY_S):
            self.player.move(90)
        elif pyxel.btnr(pyxel.KEY_S):
            self.player.stop()
        # D
        if pyxel.btnp(pyxel.KEY_D):
            self.player.move(0)
        elif pyxel.btnr(pyxel.KEY_D):
            self.player.stop()

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()