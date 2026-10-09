import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

w = pyxel.width
h = pyxel.height

# Work01
x1 = pyxel.rndi(0, w)
y1 = pyxel.rndi(0, h)
pyxel.line(0, 0, x1, y1, 7)

# Work02
x2 = pyxel.rndi(0, w)
y2 = pyxel.rndi(0, h)
pyxel.line(x1, y1, x2, y2, 8)

# Work03
x3 = pyxel.rndi(0, w)
y3 = pyxel.rndi(0, h)
pyxel.line(x2, y2, x3, y3, 9)

# TODO: Lv1
#   for文を使って、線を10本描く事
# TODO: Lv2
#   for文を使って、連続折れ線を10本描く事

# 画面表示
pyxel.show()