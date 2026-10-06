import pyxel

rabbit_x = 0

# キャラクターを描く処理
def draw_my_character(x, y, color):
    pyxel.circ(x, y, 3, color)

# 更新処理
def update():
    global rabbit_x
    rabbit_x += 1

# 描画処理
def draw():
    pyxel.cls(0)
    draw_my_character(rabbit_x, 25, 6)

# 画面初期化
pyxel.init(80, 60, title="HELLO PYXEL!!")

# Pyxel実行
pyxel.run(update, draw)
