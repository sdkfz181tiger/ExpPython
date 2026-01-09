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

MONSTER_MAX = 10
MONSTERS = [
    {"u": 32, "v": 72, "spd": 1.0},
    {"u": 48, "v": 72, "spd": 1.0},
    {"u":  0, "v": 80, "spd": 1.0},
    {"u": 16, "v": 80, "spd": 1.0},
    {"u": 32, "v": 80, "spd": 1.0}
]

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # ゲームモード
        self.game_mode = MODE_TITLE

        # プレイヤーを初期化
        self.player = sprite.PlayerSprite(START_X, START_Y, 0, 72, PLAYER_SPD)

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
        self.overlap_area(self.player)

        # モンスター
        for monster in self.monsters:
            monster.update()
            self.overlap_area(monster)
            # x プレイヤー
            if monster.intersects(self.player):
                self.game_mode = MODE_GAME_OVER

    def draw(self):
        """ 描画処理 """
        pyxel.cls(0)

        # タイルマップ
        pyxel.bltm(0, 0, 0, 0, 128, 192, 128, 0)

        # プレイヤーを描画
        self.player.draw()

        # モンスターを描画
        for monster in self.monsters:
            monster.draw()

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

        # モンスター
        self.monsters = []
        for i in range(30):
            item = random.choice(MONSTERS)
            x = random.randint(0, W)
            y = random.randint(0, H)
            u = item["u"]
            v = item["v"]
            spd = item["spd"]
            monster = sprite.Monster(x, y, u, v, spd)
            self.monsters.append(monster)

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

    def overlap_area(self, spr):
        """ オーバーラップ """
        if W < spr.x: spr.x = 0
        if spr.x < 0: spr.x = W
        if H < spr.y: spr.y = 0
        if spr.y < 0: spr.y = H

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()