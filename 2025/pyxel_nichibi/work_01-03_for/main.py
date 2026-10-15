import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

# for文
for i in range(5):
    x = i * 10
    y = 0
    pyxel.text(x, y, str(x), 7) # 白

# 画面表示
pyxel.show()