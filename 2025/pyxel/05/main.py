# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite # spriteモジュールをインポート

W, H = 160, 120
SHIP_SPD = 1.4 # プレイヤーの速度

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # プレイヤーを初期化
        self.ship = sprite.ShipSprite(W/2, H - 40)
        #deg = 0 if random.random()<0.5 else 180
        #self.ship.move(SHIP_SPD, deg)

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("shooter.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # プレイヤーを更新
        self.ship.update()

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

        # プレイヤーを描画
        self.ship.draw()

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()