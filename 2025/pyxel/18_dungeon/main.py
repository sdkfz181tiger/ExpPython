# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")

        # タイルマップスクロール位置
        self.scroll_u = 0
        self.scroll_v = 128

        pyxel.run(self.update, self.draw) # Pyxel実行

    def update(self):
        """ 更新処理 """
        # タイルマップスクロール
        if pyxel.btn(pyxel.KEY_RIGHT):
            self.scroll_u += 1
        if pyxel.btn(pyxel.KEY_LEFT):
            self.scroll_u -= 1

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # タイルマップ
        # x, y, tm, u, v, w, h, colkey=None, rotate=0, scale=1
        pyxel.bltm(0, 0, 0, self.scroll_u, self.scroll_v, 128, 128)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()