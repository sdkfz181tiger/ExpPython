# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random

W, H = 160, 120

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("my_resource.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """
        # スコアのテスト
        self.score += 1

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()