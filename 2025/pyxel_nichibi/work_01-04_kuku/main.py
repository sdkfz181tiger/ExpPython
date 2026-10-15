import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

# 二重になったfor文
for i in range(1, 10):
    print(f"{i}の段")
    y = i * 10
    print(f"yは、{y}")
    for j in range(1, 10):
        x = j * 10
        print(f"  xは、{x}")
        num = i * j
        pyxel.text(x, y, str(num), 7)

# 画面表示
pyxel.show()