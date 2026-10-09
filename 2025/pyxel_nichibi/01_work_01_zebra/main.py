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
#   縞々模様を作る
# TODO: Lv2
#   トリコロール
# TODO: Lv3
#   虹色模様を作る

# 画面表示
pyxel.show()