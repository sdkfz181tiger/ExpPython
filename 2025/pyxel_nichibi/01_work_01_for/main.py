import pyxel

# Pyxel初期化
pyxel.init(120, 90, title="Hello, Pyxel!!")

# Work01
for i in range(5):
    x = i * 10
    y = 0
    pyxel.text(x, y, str(x), 7) # 白

# 課題
# TODO: Lv1
#   白、黒...で縞模様を作る事
# TODO: Lv2
#   赤、緑、青... の順で縞模様を作る事
# TODO: Lv3
#   7色の虹色模様を作る事

# 画面表示
pyxel.show()