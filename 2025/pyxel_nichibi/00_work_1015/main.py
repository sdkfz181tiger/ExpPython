import pyxel

# Pyxel初期化
pyxel.init(120, 120, title="Hello, Pyxel!!")
pyxel.load("my_resource.pyxres")

# 文字
#pyxel.text(10, 10, "HELLO, PYXEL!!", 7) # 白

# ドット絵を表示する
# x, y, イメージID, u, v, w, h, 透明カラー
pyxel.blt(0, 0, 0, 8, 0, 8, 8, 0)

# 繰り返し処理
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