# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120

MODE_TITLE = "title"
MODE_PLAY = "play"
MODE_GAME_OVER = "game_over"

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # ゲームモード
        self.game_mode = MODE_TITLE

        # スコアを初期化
        self.score = 0

        # プレイヤーを初期化
        self.player = sprite.PlayerSprite(W/4, H/2)

        # トンネルを初期化
        self.tunnels = []
        tunnel = sprite.TunnelSprite(W/2 + 50, H/2, 10)
        self.tunnels.append(tunnel)

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("shooter.pyxres")
        pyxel.run(self.update, self.draw)

    def update(self):
        """ 更新処理 """

        # コントロール
        self.control()

        # プレイ中判定
        if self.game_mode != MODE_PLAY: return

        # プレイヤーを更新
        self.player.update()

        # トンネルを更新
        for tunnel in self.tunnels:
            tunnel.update()
            if(tunnel.intersects(self.player)):
                self.game_mode = MODE_GAME_OVER
                break

        # 落下判定
        if H < self.player.y: 
            self.game_mode = MODE_GAME_OVER

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # メッセージ
        if self.game_mode == MODE_TITLE:
            msg = "TAP TO PLAY"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 13)
        elif self.game_mode == MODE_GAME_OVER:
            msg = "GAME OVER"
            pyxel.text(W/2-len(msg)*2, H/2, msg, 13)

        # スコアを描画
        pyxel.text(10, 10, 
            "SCORE:{:04}".format(self.score), 12)

        # プレイヤーを描画
        self.player.draw()

        # トンネルを描画
        for tunnel in self.tunnels:
            tunnel.draw()

    def control(self):
        """ コントロール """
        if not pyxel.btnp(pyxel.KEY_SPACE): return

        # Title -> Play
        if self.game_mode == MODE_TITLE:
            self.game_mode = MODE_PLAY

        # Game Over -> Title
        if self.game_mode == MODE_GAME_OVER:
            self.game_mode = MODE_TITLE
            # Reset
            self.player.x = W/4
            self.player.y = H/2

        # Jump
        if self.game_mode == MODE_PLAY:
            self.player.jump()

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()