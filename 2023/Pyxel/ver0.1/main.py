# coding: utf-8

"""
Pyxel基礎

	色は16種類
		0 ~ 15
	
	pyxel.width: 横幅
	pyxel.height: 高さ
	pyxel.frame_count: フレームカウント
"""

import pyxel

class App:

	# 1, ゲーム画面の初期化
	def __init__(self):
		# 1-1, ゲーム画面の開始
		pyxel.init(160, 120, title="Hello Pyxel")
		# 1-2, 画像の読込
		pyxel.image(0).load(0, 0, "assets/doron_01.png")
		# 1-3, 更新を更新&描画を開始
		pyxel.run(self.update, self.draw)

	# 2, ゲーム画面の更新
	def update(self):
		if pyxel.btnp(pyxel.KEY_Q):# Qが押されたら
			pyxel.quit() # ゲーム終了

	# 3, ゲーム画面の描画
	def draw(self):
		# 画面をクリアする
		pyxel.cls(0)
		# テキストの描画(x, y, 文字, 色)
		pyxel.text(55, 41, "Hello, Pyxel!", pyxel.frame_count%16)
		# 正方形を表示(x1, y1, x2, y2, 色)
		pyxel.rect(0, 0, 16, 16, pyxel.frame_count%16)
		# 画像の描画
		pyxel.blt(30, 30, 0, 0, 0, 64, 64)

App()