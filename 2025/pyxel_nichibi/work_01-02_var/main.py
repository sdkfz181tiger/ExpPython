import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

# 変数を使って絵を描く
x = pyxel.width / 2
y = pyxel.height / 2

pyxel.circb(x, y, 12, 7)

pyxel.rect(x-5, y-4, 4, 4, 7)
pyxel.rect(x-3, y-2, 2, 2, 2)

pyxel.rect(x+2, y-4, 4, 4, 7)
pyxel.rect(x+4, y-2, 2, 2, 2)

pyxel.circb(x, y+2, 2, 7)

pyxel.line(x-4, y+7, x+4, y+7, 7)

# 課題
# TODO: Lv1
#   変数を使ってニコニコマークを描く事

# 画面表示
pyxel.show()