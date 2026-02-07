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
SCORE_IJIKE = 40

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
            0, 0, 0, 8, 1.8)
        self.player.set_center(W/2, H/2)

        # Enemy
        self.enemy = sprite.EnemySprite(
            0, 0, 0, 40, 1.2, self.player)
        self.enemy.set_center(0, H/2)

        # Dots
        self.dots = []
        pad_x = W / TOTAL_DOTS
        for i in range(TOTAL_DOTS):
            x = i * pad_x + pad_x / 2
            y = H / 2
            power_flg = i == 0 # Power or Normal
            dot = sprite.DotSprite(0, 0, 0, 16, power_flg)
            dot.set_center(x, y)
            self.dots.append(dot)

        # Pyxelの起動
        pyxel.init(W, H, title="Hello, Pyxel!!")
        pyxel.load("pacman.pyxres")
        pyxel.run(self.update, self.draw) # Pyxel実行

    def update(self):
        """ 更新処理 """

        self.control() # Control
        if self.mode != MODE_GAME_PLAY: return

        # Player
        self.player.update()
        self.overlap_horizontal(self.player) # Overlap

        # Enemy
        self.enemy.update()
        self.overlap_horizontal(self.enemy) # Overlap

        # Dots
        for dot in self.dots:
            dot.update()
            # Contains and Sleep
            if dot.is_sleep(): continue
            if self.player.contains_center(dot):
                self.score += SCORE_DOT # Score
                dot.sleep()
                if dot.is_power():
                    self.enemy.ijike_on() # Ijike(On)

        # Awake all dots
        if self.is_sleep_dots():
            self.awake_dots()

        # GameOver
        if self.player.contains_center(self.enemy):
            if self.enemy.is_ijike():
                self.score += SCORE_IJIKE # Score
                self.enemy.set_center(0, H/2) # Reset
                self.enemy.ijike_off() # Ijike(Off)
            else:
                self.game_over() # Game Over
            
    def draw(self):
        """ 描画処理 """
        pyxel.cls(4)

        # Road
        pyxel.rect(0, H/2-8, W, 16, 0)

        # Dots
        for dot in self.dots:
            dot.draw()
        # Player
        self.player.draw()
        # Enemy
        self.enemy.draw()

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
            self.player.go_random() # Go
            self.enemy.go_random()
            return

        # Play
        if self.mode == MODE_GAME_PLAY:
            self.player.turn() # Turn
            return

        # Over to Ready
        if self.mode == MODE_GAME_OVER:
            self.mode = MODE_GAME_READY
            self.msg = "GAME READY!?"
            self.player.set_center(W/2, H/2) # Reset
            self.enemy.set_center(0, H/2)
            self.awake_dots() # Awake
            return

    def overlap_horizontal(self, spr):
        if spr.x < 0: spr.x = W
        if W < spr.x: spr.x = 0

    def game_over(self):
        self.mode = MODE_GAME_OVER
        self.msg = "GAME OVER!!"
        self.player.stop() # Stop
        self.enemy.stop()

    def is_sleep_dots(self):
        for dot in self.dots:
            if not dot.is_sleep(): return False
        return True

    def awake_dots(self):
        for dot in self.dots:
            dot.awake()
        # Swap
        other = random.choice(self.dots)
        self.dots[0].swap_position(other)

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()