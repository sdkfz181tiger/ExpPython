import pyxel

x = 0
y = 0

# 更新処理
def update():
    global x, y
    x += 1
    y += 1

# 描画処理
def draw():
    pyxel.cls(0)
    pyxel.circ(x, y, 4, 7)

# Pyxel初期化
pyxel.init(80, 60, title="HELLO PYXEL!!")

# Pyxel実行
pyxel.run(update, draw)
