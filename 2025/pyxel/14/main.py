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

        # ゲームオーバーフラグ
        self.game_over_flg = False

        # スコアを初期化
        self.score = 0

        # プレイヤーを初期化
        self.player = sprite.PlayerSprite(W/2, H/2)

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("shooter.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # ゲームオーバー
        if self.game_over_flg:
            return

        # プレイヤーを更新
        self.player.update()
        self.control()

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # ゲームオーバー
        if self.game_over_flg:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 13)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

        # プレイヤーを描画
        self.player.draw()

    def control(self):
        """ コントロール """
        if pyxel.btnp(pyxel.KEY_SPACE):
            self.player.jump()

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()