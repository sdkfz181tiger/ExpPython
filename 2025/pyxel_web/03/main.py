# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120

MODE_GAME_READY = "mode_game_ready"
MODE_GAME_PLAY = "mode_game_play"
MODE_GAME_OVER = "mode_game_over"

TOTAL_DOTS = 12
SCORE_DOT = 10

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # Mode
        self.mode = MODE_GAME_READY

        # Message
        self.msg = "READY!?"

        # Player
        self.player = sprite.PlayerSprite(
            0, 0, 0, 8, 2.2)
        self.player.set_center(W/2, H/2)

        # Dots
        self.dots = []
        pad_x = W / TOTAL_DOTS
        power_index = random.randint(0, TOTAL_DOTS)
        for i in range(TOTAL_DOTS):
            power_flg = i == power_index # Power or Normal
            x = i * pad_x + pad_x / 2
            y = H / 2
            v = 24 if power_flg else 16
            dot = sprite.DotSprite(0, 0, 0, v, power_flg)
            dot.set_center(x, y)
            self.dots.append(dot)

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("pacman.pyxres")
        pyxel.run(self.update, self.draw) # Pyxel実行

    def update(self):
        """ 更新処理 """

        self.control() # Control

        # Player
        self.player.update()
        self.overlap_horizontal(self.player) # Overlap

        # Dots
        for dot in self.dots:
            dot.update()
            # Contains and Sleep
            if dot.is_sleep(): continue
            if self.player.contains_center(dot):
                dot.sleep()
                self.score += SCORE_DOT # Score

    def draw(self):
        """ 描画処理 """
        pyxel.cls(2)

        # Player
        self.player.draw()

        # Dots
        for dot in self.dots:
            dot.draw()

        # Score
        pyxel.text(10, 10, 
            "SCORE:{:03}".format(self.score), 7)

        # Message
        pyxel.text(W/2, 10, 
            "MODE:{}".format(self.msg), 7)

    def control(self):
        """ コントロール """
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): return

        # Ready to Play
        if self.mode == MODE_GAME_READY:
            self.mode = MODE_GAME_PLAY
            self.msg = "GAME PLAY!!"
            return

        # Play to Over
        if self.mode == MODE_GAME_PLAY:
            self.mode = MODE_GAME_OVER
            self.msg = "GAME OVER!?"
            #self.player.turn() # Turn
            return

        # Over to Ready
        if self.mode == MODE_GAME_OVER:
            self.mode = MODE_GAME_READY
            self.msg = "GAME READY!?"
            return

    def overlap_horizontal(self, spr):
        if spr.x < 0: spr.x = W
        if W < spr.x: spr.x = 0

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()