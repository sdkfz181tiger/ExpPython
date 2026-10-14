import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

# 文字
pyxel.text(10, 10, "HELLO, PYXEL!!", 7) # 白

# 点
pyxel.pset(10, 20, 3)

# 線
pyxel.line(10, 30, 40, 40, 4)

# 四角
pyxel.rect(10, 50, 30, 10, 5)
pyxel.rectb(10, 65, 30, 10, 6)

# 円
pyxel.circ(60, 30, 10, 7)
pyxel.circb(90, 30, 10, 8)

# 楕円
pyxel.elli(50, 55, 20, 10, 9)
pyxel.ellib(85, 50, 10, 20, 10)

# 課題
# TODO: Lv1
#   アンパンマンを描く事

# 画面表示
pyxel.show()