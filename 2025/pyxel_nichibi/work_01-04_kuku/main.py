import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

# Work01
for i in range(5):
    x = i * 10
    y = 0
    pyxel.text(x, y, str(x), 7) # 白

# Work02
for i in range(5):
    x = 0
    y = i * 10
    pyxel.text(x, y, str(y), 8) # 赤

# Work03
for i in range(5):
    x = i * 10
    y = i * 10
    pyxel.text(x, y, str(i), 3) # 青

# 画面表示
pyxel.show()