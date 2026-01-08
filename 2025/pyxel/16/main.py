# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120

START_X = W / 2
START_Y = H / 2 - 10

MODE_TITLE = "title"
MODE_PLAY = "play"
MODE_GAME_OVER = "game_over"

PLAYER_SPD = 1.4

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # ゲームモード
        self.game_mode = MODE_TITLE

        # プレイヤーを初期化
        self.player = sprite.PlayerSprite(START_X, START_Y, 0, 72)

        # ステージを初期化
        self.reset()

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("vampire.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # コントロール
        self.control()

        # プレイ中判定
        if self.game_mode != MODE_PLAY: return

        # プレイヤーを更新
        self.player.update()

        # 落下判定
        #if H < self.player.y: 
        #   self.game_mode = MODE_GAME_OVER

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # タイルマップ
        pyxel.bltm(0, 0, 0, 0, 128, 192, 128, 0)

        # プレイヤーを描画
        self.player.draw()

        # メッセージ
        if self.game_mode == MODE_TITLE:
            msg = "SPACE TO PLAY"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 7)
            msg = "CONTROL: WASD"
            pyxel.text(W/2-len(msg)*2, H/2+10, msg, 7)
        elif self.game_mode == MODE_GAME_OVER:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 7)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 7)

    def reset(self):
        """ ステージを初期化 """

        # プレイヤー
        self.player.x = START_X
        self.player.y = START_Y

    def control(self):
        """ コントロール """

        # ゲームループ
        if pyxel.btnp(pyxel.KEY_SPACE):

            # Title -> Play
            if self.game_mode == MODE_TITLE:
                self.game_mode = MODE_PLAY

            # Game Over -> Title
            if self.game_mode == MODE_GAME_OVER:
                self.game_mode = MODE_TITLE
                # Reset
                self.reset()

            return

        # プレイヤー
        if self.game_mode == MODE_PLAY:

            # W
            if pyxel.btnp(pyxel.KEY_W):
                self.player.go_up(PLAYER_SPD)
            elif pyxel.btnr(pyxel.KEY_W):
                self.player.stop()
            # A
            if pyxel.btnp(pyxel.KEY_A):
                self.player.go_left(PLAYER_SPD)
            elif pyxel.btnr(pyxel.KEY_A):
                self.player.stop()
            # S
            if pyxel.btnp(pyxel.KEY_S):
                self.player.go_down(PLAYER_SPD)
            elif pyxel.btnr(pyxel.KEY_S):
                self.player.stop()
            # D
            if pyxel.btnp(pyxel.KEY_D):
                self.player.go_right(PLAYER_SPD)
            elif pyxel.btnr(pyxel.KEY_D):
                self.player.stop()

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()