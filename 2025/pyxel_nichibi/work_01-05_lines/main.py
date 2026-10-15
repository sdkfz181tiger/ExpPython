import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

w = pyxel.width
h = pyxel.height

# Line
x1 = pyxel.rndi(0, w)
y1 = pyxel.rndi(0, h)
pyxel.line(0, 0, x1, y1, 7)

# 画面表示
pyxel.show()