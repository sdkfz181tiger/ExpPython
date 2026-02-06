# coding: utf-8

"""
かじるプログラミング_pyxel
"""

import pyxel
import math
import random
import sprite

W, H = 160, 120
TOTAL_DOTS = 12

# Game
class Game:
    def __init__(self):
        """ コンストラクタ """

        # スコアを初期化
        self.score = 0

        # Player
        self.player = sprite.PlayerSprite(
        	0, 0, 0, 8, 2.2)
        self.player.set_center(W/2, H/2)

        # Dots
        self.dots = []
        pad_x = W / TOTAL_DOTS
        for i in range(TOTAL_DOTS):
        	x = i * pad_x + pad_x / 2
        	y = H / 2
        	dot = sprite.DotSprite(0, 0, 0, 16)
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

    def draw(self):
        """ 描画処理 """
        pyxel.cls(2)

        # Player
        self.player.draw()

        # Dots
        for dot in self.dots:
        	dot.draw()

    def control(self):
        """ コントロール """
        if not pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT): return
        print("Click!!")
        self.player.turn() # Turn

    def overlap_horizontal(self, spr):
    	if spr.x < 0: spr.x = W
    	if W < spr.x: spr.x = 0

def main():
    """ メイン処理 """
    Game()

if __name__ == "__main__":
    main()