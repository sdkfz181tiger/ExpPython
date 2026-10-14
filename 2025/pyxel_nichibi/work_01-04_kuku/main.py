import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

# Work01
for i in range(5):
    for j in range(2):
        x = i * 10
        y = j * 10
        pyxel.text(x, y, str(x), 7) # 白

# 画面表示
pyxel.show()